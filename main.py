"""Publish lines from a text file to a Discord channel via webhook."""

from __future__ import annotations

import argparse
import os
import sys
import time
from collections.abc import Iterable, Sequence
from pathlib import Path

import requests

DEFAULT_DELAY_SECONDS = 1.5
DEFAULT_TIMEOUT_SECONDS = 15.0
DEFAULT_MAX_RETRIES = 3


class PublishError(RuntimeError):
    """Raised when a message cannot be delivered safely."""


def read_messages(path: Path) -> list[str]:
    """Return non-empty, stripped lines from *path*."""
    try:
        return [
            line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()
        ]
    except OSError as exc:
        raise PublishError(f"Could not read input file: {path}") from exc


def send_message(
    session: requests.Session,
    webhook_url: str,
    message: str,
    *,
    timeout: float = DEFAULT_TIMEOUT_SECONDS,
    max_retries: int = DEFAULT_MAX_RETRIES,
) -> None:
    """Send one message and retry Discord rate limits or transient failures."""
    for attempt in range(max_retries + 1):
        try:
            response = session.post(
                webhook_url,
                json={"content": message},
                timeout=timeout,
            )
        except requests.RequestException as exc:
            if attempt == max_retries:
                raise PublishError("Discord request failed after retries") from exc
            time.sleep(min(2**attempt, 8))
            continue

        if 200 <= response.status_code < 300:
            return

        if response.status_code == 429 and attempt < max_retries:
            try:
                retry_after = float(response.json().get("retry_after", 1))
            except (TypeError, ValueError, requests.JSONDecodeError):
                retry_after = 1.0
            time.sleep(max(retry_after, 0.0))
            continue

        if response.status_code >= 500 and attempt < max_retries:
            time.sleep(min(2**attempt, 8))
            continue

        raise PublishError(f"Discord rejected a message with HTTP {response.status_code}")

    raise PublishError("Discord request failed after retries")


def publish_messages(
    messages: Iterable[str],
    webhook_url: str,
    *,
    delay: float = DEFAULT_DELAY_SECONDS,
    reverse: bool = True,
    dry_run: bool = False,
    session: requests.Session | None = None,
) -> int:
    """Publish messages and return the number processed."""
    queue = list(messages)
    if reverse:
        queue.reverse()

    if not queue:
        return 0

    client = session or requests.Session()
    for index, message in enumerate(queue, start=1):
        if dry_run:
            print(message)
        else:
            send_message(client, webhook_url, message)
            print(f"Sent {index}/{len(queue)}")

        if index < len(queue) and delay:
            time.sleep(delay)
    return len(queue)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Publish non-empty lines from a text file to a Discord webhook."
    )
    parser.add_argument("file", type=Path, help="UTF-8 text file, one message or URL per line")
    parser.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_DELAY_SECONDS,
        help=f"seconds between messages (default: {DEFAULT_DELAY_SECONDS})",
    )
    parser.add_argument(
        "--forward",
        action="store_true",
        help="preserve file order instead of publishing from bottom to top",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the resulting order without contacting Discord",
    )
    return parser


def cli(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.delay < 0:
        print("error: --delay must be zero or greater", file=sys.stderr)
        return 2

    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    if not args.dry_run and not webhook_url:
        print("error: set DISCORD_WEBHOOK_URL before publishing", file=sys.stderr)
        return 2

    try:
        messages = read_messages(args.file)
        if not messages:
            print("No non-empty lines found; nothing was sent.")
            return 0
        count = publish_messages(
            messages,
            webhook_url,
            delay=args.delay,
            reverse=not args.forward,
            dry_run=args.dry_run,
        )
    except PublishError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    action = "Previewed" if args.dry_run else "Published"
    print(f"{action} {count} message(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
