<div align="center">

<img src="docs/assets/banner.svg" alt="Discord Link Publisher" width="860">

# Discord Link Publisher

**Send a text file of links or messages to Discord—reliably, in the order you choose.**

[![CI](https://github.com/egore4606/Discord-link-publisher/actions/workflows/ci.yml/badge.svg)](https://github.com/egore4606/Discord-link-publisher/actions/workflows/ci.yml)
[![CodeQL](https://github.com/egore4606/Discord-link-publisher/actions/workflows/codeql.yml/badge.svg)](https://github.com/egore4606/Discord-link-publisher/actions/workflows/codeql.yml)
[![Release](https://img.shields.io/github/v/release/egore4606/Discord-link-publisher?display_name=tag)](https://github.com/egore4606/Discord-link-publisher/releases)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e.svg)](LICENSE)

[English](README.md) · [Русский](docs/README.ru.md) · [Deutsch](docs/README.de.md)

</div>

Discord Link Publisher is a small command-line tool that reads non-empty lines from a UTF-8 text file and posts each line to a Discord channel through a webhook. It was created for exporting a YouTube playlist or link collection, but it works with any message that fits in a Discord webhook post.

## Why use it?

- 🔐 Keeps the webhook URL outside the source code and Git history.
- 🔄 Publishes bottom-to-top by default, or preserves file order with `--forward`.
- 🧯 Retries Discord rate limits, temporary server errors, and network failures.
- 👀 Includes a safe `--dry-run` preview that never contacts Discord.
- 🪶 Has no database, bot account, server, or background process to maintain.
- ✅ Ships with automated tests, linting, dependency updates, and CodeQL scanning.

## Quick start

### 1. Install

Python 3.10 or newer is required.

```bash
git clone https://github.com/egore4606/Discord-link-publisher.git
cd Discord-link-publisher
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS or Linux
source .venv/bin/activate
```

Then install the command:

```bash
python -m pip install .
```

### 2. Prepare an input file

Create `links.txt` with one URL or message per line. Blank lines are ignored.

```text
https://youtu.be/video-one
https://youtu.be/video-two
https://youtu.be/video-three
```

You can create this file manually or export playlist URLs with a browser tool such as [YouTube URL Extractor](https://chromewebstore.google.com/detail/youtube-url-extractor/jmilibpbdpajjnabchfpfmmmjgbimefo).

### 3. Preview the order

```bash
discord-link-publisher links.txt --dry-run --delay 0
```

The default sends the last non-empty line first. Add `--forward` if the first line should be posted first.

### 4. Publish

Create a webhook in **Discord → Server Settings → Integrations → Webhooks**, then expose it only to the current shell:

```powershell
# Windows PowerShell
$env:DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/…"
discord-link-publisher links.txt
```

```bash
# macOS or Linux
export DISCORD_WEBHOOK_URL='https://discord.com/api/webhooks/…'
discord-link-publisher links.txt
```

The tool prints progress without ever printing the webhook URL or Discord response body.

## Command reference

```text
usage: discord-link-publisher [-h] [--delay SECONDS] [--forward] [--dry-run] file
```

| Option | Meaning |
| --- | --- |
| `file` | UTF-8 text file, one message or URL per line |
| `--delay SECONDS` | Pause between posts; default is `1.5` seconds |
| `--forward` | Post from the first line to the last |
| `--dry-run` | Print the resulting order without contacting Discord |

You may also run the source checkout directly:

```bash
python main.py links.txt --dry-run
```

## Ordering explained

Given `one`, `two`, `three` in the file:

| Mode | Post sequence |
| --- | --- |
| Default | `three` → `two` → `one` |
| `--forward` | `one` → `two` → `three` |

Discord displays older messages above newer messages. Choose the mode based on how you want the finished channel to read.

## Security

A Discord webhook is a secret: anyone who has it can post to that channel.

- Never paste it into `main.py`, a commit, an issue, or a screenshot.
- Store it in `DISCORD_WEBHOOK_URL` only for as long as needed.
- Delete and recreate the webhook immediately if it is exposed.
- Use `--dry-run` before large imports.

Please report vulnerabilities privately according to [SECURITY.md](SECURITY.md).

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
ruff format --check .
pytest
python -m build
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution workflow and [CHANGELOG.md](CHANGELOG.md) for release notes.

## Community and support

- [Ask a question or share an idea](https://github.com/egore4606/Discord-link-publisher/discussions)
- [Report a reproducible bug](https://github.com/egore4606/Discord-link-publisher/issues/new/choose)
- [Read the support guide](SUPPORT.md)

## License

Released under the [MIT License](LICENSE).
