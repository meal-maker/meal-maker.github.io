import asyncio
import json
from datetime import datetime, timezone

from src.ai.enricher import ContentEnricher
from src.models import ContentItem, SourceType


def _run_async(coro):
    return asyncio.run(coro)


class _FakeClient:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    async def complete(self, system: str, user: str) -> str:
        self.calls.append({"system": system, "user": user})
        return self.responses.pop(0)


def _make_item() -> ContentItem:
    item = ContentItem(
        id="rss:item-1",
        source_type=SourceType.RSS,
        title="Claude 5 context engineering rules",
        url="https://example.com/item-1",
        content="content",
        author="tester",
        published_at=datetime(2026, 7, 26, 8, 0, tzinfo=timezone.utc),
    )
    item.ai_summary = "Anthropic published new guidance for context engineering with Claude 5."
    return item


def test_ensure_chinese_metadata_translates_empty_or_english_fields():
    item = _make_item()
    item.metadata.update(
        {
            "title_en": "Claude 5 context engineering rules",
            "title_zh": "Claude 5 context engineering rules",
            "detailed_summary_en": "Anthropic published new guidance for context engineering.",
            "background_en": "Context engineering manages what information is placed in model context.",
            "community_discussion_en": "Commenters debated reliability and tooling lock-in.",
        }
    )
    client = _FakeClient(
        [
            json.dumps(
                {
                    "title_zh": "Claude 5 上下文工程新规则",
                    "detailed_summary_zh": "Anthropic 发布了 Claude 5 的上下文工程新指南。",
                    "background_zh": "上下文工程是指控制模型上下文中放入哪些信息。",
                    "community_discussion_zh": "评论区讨论了可靠性与工具绑定问题。",
                },
                ensure_ascii=False,
            )
        ]
    )
    enricher = ContentEnricher(client)

    _run_async(enricher._ensure_chinese_metadata(item))

    assert item.metadata["title_zh"] == "Claude 5 上下文工程新规则"
    assert item.metadata["detailed_summary_zh"] == "Anthropic 发布了 Claude 5 的上下文工程新指南。"
    assert item.metadata["background_zh"] == "上下文工程是指控制模型上下文中放入哪些信息。"
    assert item.metadata["community_discussion_zh"] == "评论区讨论了可靠性与工具绑定问题。"
    assert len(client.calls) == 1


def test_translate_item_populates_chinese_title_and_summary():
    item = _make_item()
    client = _FakeClient(
        [
            json.dumps(
                {
                    "title_zh": "Claude 5 上下文工程规则",
                    "detailed_summary_zh": "Anthropic 发布了新的 Claude 5 上下文工程建议。",
                },
                ensure_ascii=False,
            )
        ]
    )
    enricher = ContentEnricher(client)

    _run_async(enricher._translate_item(item))

    assert item.metadata["title_zh"] == "Claude 5 上下文工程规则"
    assert item.metadata["detailed_summary_zh"] == "Anthropic 发布了新的 Claude 5 上下文工程建议。"
