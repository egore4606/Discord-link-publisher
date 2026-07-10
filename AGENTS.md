# Agent guidance

## Scope

This repository contains a one-shot Python CLI. Keep it simple: no persistent service, Discord bot account, database, or UI unless a maintainer explicitly requests that change.

## Safety invariants

- Never commit, print, or test with a real Discord webhook.
- Keep all network behavior injectable so tests remain offline.
- Preserve the default reverse-order behavior for compatibility.
- Fail clearly and with a non-zero exit code when publishing is incomplete.
- Do not include Discord response bodies in errors because they may contain sensitive context.

## Required checks

Run `ruff check .`, `ruff format --check .`, `pytest`, and `python -m build` before proposing changes. Update tests and documentation when user-facing behavior changes.
