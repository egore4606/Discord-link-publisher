# Contributing

Thank you for improving Discord Link Publisher.

## Before opening an issue

- Use Discussions for usage questions and early ideas.
- Search existing issues first.
- Never include a real Discord webhook URL, token, or private message content.
- For security concerns, follow [SECURITY.md](SECURITY.md) instead of opening a public issue.

## Development setup

```bash
git clone https://github.com/egore4606/Discord-link-publisher.git
cd Discord-link-publisher
python -m venv .venv
python -m pip install -e ".[dev]"
```

Create a focused branch and run the full local check before proposing a change:

```bash
ruff check .
ruff format --check .
pytest
python -m build
```

Tests must use fake sessions or mocks. They must never contact a real Discord webhook.

## Pull requests

- Keep each pull request focused on one change.
- Explain the problem and the resulting behavior.
- Add or update tests for behavior changes.
- Update README and CHANGELOG when users are affected.
- Ensure every required GitHub check passes.

By contributing, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md) and license your contribution under the [MIT License](LICENSE).
