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
