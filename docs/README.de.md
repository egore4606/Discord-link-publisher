<div align="center">

# Discord Link Publisher

**Links oder Nachrichten sicher und in der gewünschten Reihenfolge an Discord senden.**

[English](../README.md) · [Русский](README.ru.md) · **Deutsch**

</div>

Das Programm liest nicht leere Zeilen aus einer UTF-8-Textdatei und veröffentlicht sie nacheinander über einen Webhook in einem Discord-Kanal. Es eignet sich für YouTube-Playlists, Linksammlungen und beliebige kurze Nachrichten.

## Funktionen

- Der Webhook bleibt in einer Umgebungsvariable statt im Quellcode.
- Standardmäßig werden Zeilen von unten nach oben gesendet; `--forward` erhält die Dateireihenfolge.
- Discord-Ratenbegrenzungen sowie vorübergehende Server- und Netzwerkfehler werden wiederholt.
- `--dry-run` zeigt die Reihenfolge, ohne Discord zu kontaktieren.
- Kein Bot-Konto, keine Datenbank und kein dauerhafter Server erforderlich.

## Schnellstart

Python 3.10 oder neuer wird benötigt.

```bash
git clone https://github.com/egore4606/Discord-link-publisher.git
cd Discord-link-publisher
python -m venv .venv
python -m pip install .
```

Erstelle `links.txt` mit einem Link oder einer Nachricht pro Zeile und prüfe zuerst die Ausgabe:

```bash
discord-link-publisher links.txt --dry-run --delay 0
```

Erstelle unter **Discord → Servereinstellungen → Integrationen → Webhooks** einen Webhook und setze ihn nur für das aktuelle Terminal:

```powershell
$env:DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/…"
discord-link-publisher links.txt
```

Unter Linux oder macOS:

```bash
export DISCORD_WEBHOOK_URL='https://discord.com/api/webhooks/…'
discord-link-publisher links.txt
```

Mit `--forward` wird die erste Zeile zuerst gesendet. Das Intervall lässt sich beispielsweise mit `--delay 3` ändern.

## Sicherheit

Ein Webhook ist ein Geheimnis. Füge ihn nie in Quellcode, Git, Issues oder Screenshots ein. Wurde er offengelegt, lösche ihn sofort in Discord und erstelle einen neuen. Sicherheitslücken bitte gemäß [SECURITY.md](../SECURITY.md) melden.

Alle Optionen, Entwicklungsanweisungen und Lizenzinformationen stehen im [englischen README](../README.md).
