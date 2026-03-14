# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Paradigm

This project strictly follows **Test-Driven Development (TDD)**. All code must be written in this order:
1. Write a failing test first
2. Write the minimal code to make it pass
3. Refactor

## Git Workflow

After each significant change, create a commit. The commit message should clearly describe what was changed (e.g., `add user authentication`, `fix payment calculation bug`).

## Clarifying Questions

Always ask clarifying questions interactively before starting any task. If anything about the requirements is unclear or ambiguous, ask first — never assume.

## Library Documentation

Always use **mcp-context7** to fetch up-to-date documentation before working with any library or framework. Do not rely solely on training knowledge for library APIs.

## CLAUDE.md Maintenance

After each significant change, update this file with any important information about what was added or changed — new modules, architectural decisions, key conventions, or non-obvious implementation details.

---

## Project: Telegram Text Formatter Bot

A Telegram bot that accepts raw text, reformats it via OpenRouter LLM (Hook + Body + CTA structure), and returns platform-ready versions for Telegram and/or Instagram.

### Commands
```bash
uv sync                          # install dependencies
uv run pytest tests/ -v          # run all tests
uv run pytest tests/test_X.py::test_name -v  # run single test
uv run python bot.py             # start the bot
```

### Architecture
- `bot.py` — entry point, aiogram Dispatcher + MemoryStorage
- `handlers/text_handler.py` — FSM: receives text → shows platform keyboard → calls services → replies
- `services/ai_formatter.py` — calls OpenRouter API (gpt-4o-mini), returns `{hook, body, cta}` dict
- `services/platform_formatter.py` — pure functions: Telegram MarkdownV2 formatting and Instagram Unicode bold/italic

### Key Conventions
- `services/ai_formatter.py` initializes the OpenRouter client at module level with a "placeholder" fallback so tests can import without a real API key
- Tests mock `services.ai_formatter.client` directly
- Instagram "bold" and "italic" use Unicode mathematical alphanumeric symbols (𝗮𝗯𝗰 / 𝘢𝘣𝘤)
- Required env vars: `TELEGRAM_TOKEN`, `OPENROUTER_API_KEY` (see `.env.example`)
