# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Horizon is an AI-driven information aggregation system. It fetches news from multiple sources (Hacker News, RSS, Reddit, Telegram, GitHub), uses an LLM to score and filter items, enriches high-scoring items with web-searched background, then generates bilingual (EN/ZH) daily summaries published as a Jekyll site to GitHub Pages. This repo is a fork of `Thysrael/Horizon` deployed at `meal-maker.github.io`.

## Commands

```bash
uv sync                  # Install/refresh dependencies (uv-managed, hatchling build backend)
uv run horizon           # Run full pipeline with default time window (from config)
uv run horizon --hours 48  # Override time window
./scripts/daily-run.sh   # Local equivalent of CI: pulls, runs, deploys docs to gh-pages via worktree
```

There is no test suite or linter configured — `pyproject.toml` declares only runtime deps. Requires Python ≥3.11.

## Configuration & Secrets

- All runtime config lives in `data/config.json` (created from `data/config.example.json`). Loaded by `StorageManager.load_config()` into the pydantic `Config` model (`src/models.py`).
- API keys and email passwords are **never** in config.json directly — config stores an env-var *name* (e.g. `"api_key_env": "OPENAI_API_KEY"`) and the code reads the actual value from the environment (`os.getenv`). Load `.env` via `python-dotenv` (loaded in `src/main.py`).
- Note: there is no `.env.example` committed; create `.env` manually with the env-var names your `config.json` references (e.g. `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GITHUB_TOKEN`, plus the SMTP/IMAP password env var for email).
- `data/config.json` and `data/subscribers.json` are runtime state — do not commit real secrets/subscriber data.

## Architecture

### Pipeline (single entry point)
`src/main.py` (CLI `horizon`) → `HorizonOrchestrator.run()` in `src/orchestrator.py` is the entire workflow. It is a linear, sequential pipeline despite using async I/O:

1. **Email check** — if `config.email.enabled`, `EmailManager.check_subscriptions()` polls IMAP inbox for subscribe/unsubscribe keywords before processing.
2. **Fetch** (`_fetch_all_sources`) — opens one shared `httpx.AsyncClient` and runs all enabled scrapers concurrently via `asyncio`.
3. **Cross-source dedup** (`_merge_cross_source_duplicates`) — merges items sharing the same URL across platforms.
4. **AI analyze** (`_analyze_content`) — `ContentAnalyzer` (`src/ai/analyzer.py`) scores each item 0–10 via the configured `AIClient`.
5. **Filter** — keep items ≥ `config.filtering.ai_score_threshold`, sorted desc.
6. **Topic dedup** (`_merge_topic_duplicates`) — second semantic dedup pass on the filtered set.
7. **Enrich** (`_enrich_important_items`) — `ContentEnricher` (`src/ai/enricher.py`) does a 2nd AI pass + web search (`src/search.py`, uses `ddgs`) for background context.
8. **Summarize + emit** — for each language in `config.ai.languages`, `DailySummarizer` (`src/ai/summarizer.py`) generates Markdown, then writes to **three** sinks: `data/summaries/horizon-<date>-<lang>.md`, a Jekyll post `docs/_posts/<date>-summary-<lang>.md` (with injected front matter, H1 stripped), and email to subscribers if enabled.

### Key abstractions
- **`BaseScraper`** (`src/scrapers/base.py`) — ABC; each source (`github`, `hackernews`, `rss`, `reddit`, `telegram`) implements `async fetch(since) -> List[ContentItem]`. IDs follow `{source}:{subtype}:{native_id}`. Scrapers receive the shared `httpx.AsyncClient`.
- **`AIClient`** (`src/ai/client.py`) — ABC wrapping multiple providers (`AnthropicClient`, `OpenAIClient`, `GeminiClient`, `DoubaoClient`); `create_ai_client(config)` factory picks one by `AIProvider`. All share a `complete(system, user, temperature, max_tokens)` interface. Doubao uses the OpenAI-compatible API.
- **`ContentItem`** (`src/models.py`) — the unified data model flowing through the pipeline; AI analysis fields (`ai_score`, `ai_summary`, `ai_tags`) are populated as items progress.
- **`StorageManager`** (`src/storage/manager.py`) — file-based persistence for config, summaries, and the subscriber list (`data/subscribers.json`).
- **`EmailManager`** (`src/services/emailer.py`) — SMTP send + IMAP subscribe/unsubscribe polling (keyword-based).

### Deployment
`.github/workflows/main.yml` runs on a daily cron (`0 0 * * *` UTC) and manual dispatch: installs uv, `uv sync`, `uv run horizon --hours 48`, then commits `docs/` back to `main` via `peaceiris/actions-gh-pages` with `keep_files: true` (preserves prior summaries). `docs/` is a Jekyll site (`theme: jekyll-theme-cayman`); `_posts/` accumulates one post per language per day. The two-pipeline AI passes (analyze → enrich) are intentional — enrichment only runs on items that already passed the score threshold, so it is the expensive step gated behind filtering.

## Conventions

- All HTTP I/O is async (`httpx.AsyncClient`); the orchestrator owns the client lifetime and shares it across scrapers.
- Console output goes through `rich.Console`; keep the emoji + colored prefix style used throughout `orchestrator.py`.
- AI prompts are centralized in `src/ai/prompts.py` — edit there rather than inlining.
- Output filenames and Jekyll front-matter format are coupled between `StorageManager.save_daily_summary` and the orchestrator's post-copy logic; change both together.
