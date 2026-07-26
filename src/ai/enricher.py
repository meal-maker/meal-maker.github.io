"""Content enrichment using AI (second-pass analysis).

For items that pass the score threshold, this module:
1. Searches the web for relevant context (via DuckDuckGo)
2. Feeds search results + item content to AI to generate grounded background knowledge
"""

import asyncio
import json
import sys
import os
from typing import List, Optional
from tenacity import retry, stop_after_attempt, wait_exponential
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, MofNCompleteColumn
from ddgs import DDGS

from .client import AIClient
from .prompts import (
    CONCEPT_EXTRACTION_SYSTEM, CONCEPT_EXTRACTION_USER,
    CONTENT_ENRICHMENT_SYSTEM, CONTENT_ENRICHMENT_USER,
)
from .utils import coerce_text, has_meaningful_cjk, parse_json_response
from ..models import ContentItem


class ContentEnricher:
    """Enriches high-scoring content items with background knowledge."""

    def __init__(self, ai_client: AIClient):
        self.client = ai_client

    def _get_concurrency(self) -> int:
        """Return the configured enrichment concurrency, clamped to 1 or above."""
        config = getattr(self.client, "config", None)
        concurrency = getattr(config, "enrichment_concurrency", 1)
        return max(concurrency, 1)

    def _get_timeout_sec(self) -> float:
        """Return the per-item enrichment timeout, clamped above zero."""
        config = getattr(self.client, "config", None)
        timeout = getattr(config, "enrichment_timeout_sec", 30.0)
        return max(float(timeout), 1.0)

    def _get_fallback_timeout_sec(self) -> float:
        """Return a bounded timeout for lightweight translation fallback."""
        return min(max(self._get_timeout_sec() / 3, 5.0), 15.0)

    async def enrich_batch(self, items: List[ContentItem]) -> None:
        """Enrich items in-place with background knowledge.

        Args:
            items: Content items to enrich (modified in-place)
        """
        concurrency = self._get_concurrency()
        timeout_sec = self._get_timeout_sec()
        fallback_timeout_sec = self._get_fallback_timeout_sec()
        semaphore = asyncio.Semaphore(concurrency)

        async def _process(item: ContentItem, progress_task) -> None:
            async with semaphore:
                try:
                    await asyncio.wait_for(self._enrich_item(item), timeout=timeout_sec)
                except asyncio.TimeoutError:
                    print(
                        f"Warning: enrichment timed out for {item.id} after "
                        f"{timeout_sec:.0f}s, falling back to translation"
                    )
                    try:
                        await asyncio.wait_for(
                            self._translate_item(item),
                            timeout=fallback_timeout_sec,
                        )
                    except asyncio.TimeoutError:
                        print(
                            f"Warning: translation fallback timed out for {item.id} after "
                            f"{fallback_timeout_sec:.0f}s, skipping item"
                        )
                except Exception as e:
                    print(f"Error enriching item {item.id}: {e}, falling back to translation")
                    try:
                        await asyncio.wait_for(
                            self._translate_item(item),
                            timeout=fallback_timeout_sec,
                        )
                    except asyncio.TimeoutError:
                        print(
                            f"Warning: translation fallback timed out for {item.id} after "
                            f"{fallback_timeout_sec:.0f}s, skipping item"
                        )
            progress.advance(progress_task)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            transient=True,
        ) as progress:
            task = progress.add_task("Enriching", total=len(items))
            coros = [
                _process(item, task) for item in items
            ]
            await asyncio.gather(*coros)

    async def _web_search(self, query: str, max_results: int = 3) -> list:
        """Search the web for context via DuckDuckGo.

        Returns:
            List of dicts with keys: title, url, body
        """
        try:
            # Suppress primp "Impersonate ... does not exist" stderr warning
            stderr = sys.stderr
            sys.stderr = open(os.devnull, "w")
            try:
                ddgs = DDGS()
                results = await asyncio.to_thread(ddgs.text, query, max_results=max_results)
            finally:
                sys.stderr.close()
                sys.stderr = stderr
        except Exception:
            return []

        return [
            {"title": r.get("title", ""), "url": r.get("href", ""), "body": r.get("body", "")}
            for r in (results or [])
        ]

    @staticmethod
    def _parse_json_response(response: str) -> Optional[dict]:
        """Try multiple strategies to extract a JSON object from an AI response.

        Returns the parsed dict, or None if all strategies fail.
        """
        return parse_json_response(response)

    @staticmethod
    def _store_text(item: ContentItem, key: str, value: object) -> None:
        text = coerce_text(value)
        if text:
            item.metadata[key] = text

    def _store_enrichment_result(self, item: ContentItem, result: dict) -> None:
        """Normalize and persist enrichment fields."""
        for lang in ("en", "zh"):
            self._store_text(item, f"title_{lang}", result.get(f"title_{lang}"))

            parts = []
            for field in ("whats_new", "why_it_matters", "key_details"):
                text = coerce_text(result.get(f"{field}_{lang}"))
                if text:
                    parts.append(text)
            if parts:
                item.metadata[f"detailed_summary_{lang}"] = " ".join(parts)

            self._store_text(item, f"background_{lang}", result.get(f"background_{lang}"))
            self._store_text(
                item,
                f"community_discussion_{lang}",
                result.get(f"community_discussion_{lang}"),
            )

    async def _translate_fields_to_zh(self, fields: dict[str, str]) -> dict[str, str]:
        """Translate arbitrary text fields to Simplified Chinese."""
        payload = {key: text for key, text in fields.items() if coerce_text(text)}
        if not payload:
            return {}

        example = {key: f"<{key} 的中文内容>" for key in payload}
        response = await self.client.complete(
            system=(
                "You are a translator. Translate every value into Simplified Chinese. "
                "Keep the exact same JSON keys. Return only valid JSON."
            ),
            user=(
                "Translate the following JSON values into Simplified Chinese. "
                "Do not leave any sentence in English except necessary proper nouns or acronyms.\n\n"
                f"Input JSON:\n{json.dumps(payload, ensure_ascii=False, indent=2)}\n\n"
                f"Return JSON:\n{json.dumps(example, ensure_ascii=False, indent=2)}"
            ),
        )
        result = self._parse_json_response(response)
        if not result:
            return {}

        translated: dict[str, str] = {}
        for key in payload:
            text = coerce_text(result.get(key))
            if text:
                translated[key] = text
        return translated

    async def _ensure_chinese_metadata(self, item: ContentItem) -> None:
        """Backfill missing or invalid Chinese fields from English fields."""
        candidates = {
            "title_zh": coerce_text(item.metadata.get("title_en")) or item.title,
            "detailed_summary_zh": (
                coerce_text(item.metadata.get("detailed_summary_en"))
                or item.ai_summary
                or item.title
            ),
            "background_zh": coerce_text(item.metadata.get("background_en")),
            "community_discussion_zh": coerce_text(item.metadata.get("community_discussion_en")),
        }

        missing: dict[str, str] = {}
        for key, source_text in candidates.items():
            if not source_text:
                continue
            current_text = coerce_text(item.metadata.get(key))
            if not has_meaningful_cjk(current_text):
                missing[key] = source_text

        if not missing:
            return

        translated = await self._translate_fields_to_zh(missing)
        for key, text in translated.items():
            if has_meaningful_cjk(text):
                item.metadata[key] = text

    async def _extract_concepts(self, item: ContentItem, content_text: str) -> List[str]:
        """Ask AI to identify concepts that need explanation.

        Args:
            item: Content item
            content_text: Extracted content text

        Returns:
            List of search queries for concepts that need explanation
        """
        user_prompt = CONCEPT_EXTRACTION_USER.format(
            title=item.title,
            summary=item.ai_summary or item.title,
            tags=", ".join(item.ai_tags) if item.ai_tags else "",
            content=content_text[:1000],
        )

        try:
            response = await self.client.complete(
                system=CONCEPT_EXTRACTION_SYSTEM,
                user=user_prompt,
            )
            result = self._parse_json_response(response)
            if result is None:
                return []
            queries = result.get("queries", [])
            return queries[:3]
        except Exception:
            return []

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(min=2, max=10)
    )
    async def _enrich_item(self, item: ContentItem) -> None:
        """Enrich a single item with background knowledge.

        Steps:
        1. Ask AI which concepts in the news need explanation
        2. Search the web for those concepts
        3. Ask AI to generate background based on search results

        Args:
            item: Content item to enrich (modified in-place via metadata)
        """
        # Extract content text and comments separately
        content_text = ""
        comments_text = ""
        if item.content:
            if "--- Top Comments ---" in item.content:
                main, comments_part = item.content.split("--- Top Comments ---", 1)
                content_text = main.strip()[:4000]
                comments_text = comments_part.strip()[:2000]
            else:
                content_text = item.content[:4000]

        # Step 1: AI identifies concepts to explain
        queries = await self._extract_concepts(item, content_text)

        # Step 2: Search web for each concept
        all_results = []
        web_sections = []
        search_tasks = [self._web_search(query) for query in queries]
        search_results = await asyncio.gather(*search_tasks, return_exceptions=True)
        for query, results in zip(queries, search_results):
            if isinstance(results, Exception):
                continue
            all_results.extend(results)
            if results:
                lines = [f"- [{r['title']}]({r['url']}): {r['body']}" for r in results]
                web_sections.append(f"**{query}:**\n" + "\n".join(lines))
        web_context = "\n\n".join(web_sections) if web_sections else ""

        # Index of available URLs for citation validation
        available_urls = {r["url"]: r["title"] for r in all_results if r.get("url")}

        # Step 3: AI generates background grounded in search results
        user_prompt = CONTENT_ENRICHMENT_USER.format(
            title=item.title,
            url=str(item.url),
            summary=item.ai_summary or item.title,
            score=item.ai_score or 0,
            reason=item.ai_reason or "",
            tags=", ".join(item.ai_tags) if item.ai_tags else "",
            content=content_text,
            comments_section=f"\n**Community Comments:**\n{comments_text}" if comments_text else "",
            web_context=web_context or "No web search results available.",
        )

        response = await self.client.complete(
            system=CONTENT_ENRICHMENT_SYSTEM,
            user=user_prompt,
        )

        # Parse JSON response with robust fallback
        result = self._parse_json_response(response)
        if result is None:
            # Gracefully degrade: fall back to a lightweight translation
            # instead of dropping the item untranslated.
            print(f"Warning: could not parse enrichment response for {item.id}, falling back to translation")
            await self._translate_item(item)
            return

        self._store_enrichment_result(item, result)
        await self._ensure_chinese_metadata(item)

        # Store citation sources — only URLs that actually came from our search results
        if result.get("sources") and available_urls:
            valid = [
                {"url": u, "title": available_urls[u]}
                for u in result["sources"]
                if u in available_urls
            ]
            if valid:
                item.metadata["sources"] = valid

        # Backward-compatible fallback fields (English as default)
        item.metadata["detailed_summary"] = item.metadata.get("detailed_summary_en", "")
        item.metadata["background"] = item.metadata.get("background_en", "")
        item.metadata["community_discussion"] = item.metadata.get("community_discussion_en", "")

    async def _translate_item(self, item: ContentItem) -> None:
        """Lightweight translation fallback: when full enrichment fails, at least
        translate the title and summary to Chinese so the item is not dropped."""
        try:
            translated = await self._translate_fields_to_zh(
                {
                    "title_zh": item.title,
                    "detailed_summary_zh": item.ai_summary or item.title,
                }
            )
            if translated.get("title_zh"):
                item.metadata["title_zh"] = translated["title_zh"]
            if translated.get("detailed_summary_zh"):
                item.metadata["detailed_summary_zh"] = translated["detailed_summary_zh"]
        except Exception:
            pass
