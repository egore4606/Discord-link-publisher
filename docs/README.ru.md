<div align="center">

# Discord Link Publisher

**Отправляйте список ссылок или сообщений в Discord безопасно и в нужном порядке.**

[English](../README.md) · **Русский** · [Deutsch](README.de.md)

</div>

Программа читает непустые строки из текстового файла UTF-8 и по очереди публикует их в канал Discord через webhook. Она подходит для переноса плейлистов YouTube, подборок ссылок и любых коротких текстовых сообщений.

## Возможности

- Webhook хранится в переменной окружения, а не в исходном коде.
- По умолчанию строки отправляются снизу вверх; `--forward` сохраняет порядок файла.
- Ограничения частоты Discord, временные ошибки сервера и сети повторяются автоматически.
- `--dry-run` позволяет проверить порядок без обращения к Discord.
- Не нужны бот, база данных или постоянно работающий сервер.

## Быстрый запуск

Требуется Python 3.10 или новее.

```bash
git clone https://github.com/egore4606/Discord-link-publisher.git
cd Discord-link-publisher
python -m venv .venv
python -m pip install .
```

Создайте `links.txt`, по одной ссылке или сообщению на строку, и сначала проверьте результат:

```bash
discord-link-publisher links.txt --dry-run --delay 0
```

Создайте webhook в **Discord → Настройки сервера → Интеграции → Webhooks** и задайте его только в текущем терминале:

```powershell
$env:DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/…"
discord-link-publisher links.txt
```

В Linux или macOS:

```bash
export DISCORD_WEBHOOK_URL='https://discord.com/api/webhooks/…'
discord-link-publisher links.txt
```

Добавьте `--forward`, чтобы сначала была отправлена первая строка. Интервал меняется параметром `--delay`, например `--delay 3`.

## Безопасность

Webhook — это секрет. Не добавляйте его в код, Git, Issue или скриншоты. Если адрес стал известен посторонним, сразу удалите webhook в Discord и создайте новый. Уязвимости сообщайте по инструкции в [SECURITY.md](../SECURITY.md).

Полное описание параметров, разработки и лицензии находится в [основном README](../README.md).
