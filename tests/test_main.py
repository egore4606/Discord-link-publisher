from pathlib import Path

import pytest
import requests

import main


class FakeResponse:
    def __init__(self, status_code: int, body: dict | None = None):
        self.status_code = status_code
        self._body = body or {}

    def json(self):
        return self._body


class FakeSession:
    def __init__(self, responses):
        self.responses = iter(responses)
        self.messages = []

    def post(self, url, *, json, timeout):
        self.messages.append((url, json, timeout))
        response = next(self.responses)
        if isinstance(response, Exception):
            raise response
        return response


def test_read_messages_ignores_blank_lines(tmp_path: Path):
    source = tmp_path / "links.txt"
    source.write_text(" first \n\nsecond\n", encoding="utf-8")

    assert main.read_messages(source) == ["first", "second"]


def test_read_messages_wraps_file_errors(tmp_path: Path):
    with pytest.raises(main.PublishError, match="Could not read"):
        main.read_messages(tmp_path / "missing.txt")


def test_publish_reverses_messages_by_default(monkeypatch):
    monkeypatch.setattr(main.time, "sleep", lambda _seconds: None)
    session = FakeSession([FakeResponse(204), FakeResponse(204)])

    count = main.publish_messages(
        ["one", "two"],
        "https://example.invalid/webhook",
        delay=0,
        session=session,
    )

    assert count == 2
    assert [call[1]["content"] for call in session.messages] == ["two", "one"]


def test_send_message_retries_rate_limit(monkeypatch):
    sleeps = []
    monkeypatch.setattr(main.time, "sleep", sleeps.append)
    session = FakeSession([FakeResponse(429, {"retry_after": 0.25}), FakeResponse(204)])

    main.send_message(session, "https://example.invalid/webhook", "hello")

    assert sleeps == [0.25]
    assert len(session.messages) == 2


def test_send_message_does_not_leak_response_body():
    session = FakeSession([FakeResponse(401, {"secret": "should-not-appear"})])

    with pytest.raises(main.PublishError, match="HTTP 401") as error:
        main.send_message(session, "https://example.invalid/webhook", "hello")

    assert "secret" not in str(error.value)


def test_send_message_wraps_network_error(monkeypatch):
    monkeypatch.setattr(main.time, "sleep", lambda _seconds: None)
    session = FakeSession([requests.ConnectionError("offline")] * 4)

    with pytest.raises(main.PublishError, match="after retries"):
        main.send_message(session, "https://example.invalid/webhook", "hello")


def test_cli_requires_webhook_except_for_dry_run(tmp_path: Path, monkeypatch, capsys):
    source = tmp_path / "links.txt"
    source.write_text("https://example.com\n", encoding="utf-8")
    monkeypatch.delenv("DISCORD_WEBHOOK_URL", raising=False)

    assert main.cli([str(source)]) == 2
    assert "DISCORD_WEBHOOK_URL" in capsys.readouterr().err
    assert main.cli([str(source), "--dry-run", "--delay", "0"]) == 0
