import json
import time
import requests
from pathlib import Path

# ---------- CONFIGURATION -----------------------------------------------
# Replace with your own Discord webhook URL
WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"

# Path to the text file containing YouTube links (one per line)
FILE_PATH = Path(r"C:\\Users\\YourName\\Downloads\\Links.txt")

# Delay (in seconds) between sending each message to prevent rate limiting
DELAY_SEC = 1.5
# ------------------------------------------------------------------------

def send_line(line: str) -> None:
    """Send a single line (YouTube link) to the Discord channel."""
    payload = {"content": line}
    try:
        res = requests.post(
            WEBHOOK_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            timeout=10
        )
        if res.status_code >= 400:
            print(f"Error {res.status_code}: {res.text}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def main():
    """Read links from file and send them to Discord in reverse order."""
    if not FILE_PATH.exists():
        print(f"Error: File not found → {FILE_PATH}")
        return

    with FILE_PATH.open("r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]  # remove empty lines

    for line in reversed(lines):
        send_line(line)
        time.sleep(DELAY_SEC)

if __name__ == "__main__":
    main()
