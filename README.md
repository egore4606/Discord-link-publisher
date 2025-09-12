# YouTube Playlist to Discord

This project provides a simple Python script that automatically sends all YouTube video links from a text file into a Discord channel via a webhook. It is useful if you want to share an entire playlist or a collection of videos with your community in just a few clicks.

---

## ✨ Features

- Reads video links from a `.txt` file (exported with [YouTube URL Extractor](https://chromewebstore.google.com/detail/youtube-url-extractor/jmilibpbdpajjnabchfpfmmmjgbimefo))  
- Sends each link to a Discord channel through a **Discord Webhook**  
- Maintains order: links are sent in **reverse order**, so the first video appears at the top of the channel  
- Configurable **delay between messages** to avoid spam rate limits  
- Simple, lightweight, and requires only Python  

---

## 🛠 Requirements

- Python 3.7+  
- [Requests library](https://pypi.org/project/requests/)  

Install requirements:  

```bash
pip install requests
```

---

## ⚙️ Setup

1. **Clone or download this repository.**  

2. **Edit the configuration** inside `links.py`:  

```python
WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"  
FILE_PATH   = Path(r"C:\Users\YourName\Downloads\Links.txt")  
DELAY_SEC   = 1.5
```

- `WEBHOOK_URL` → Replace with your Discord webhook URL (create one in *Server Settings → Integrations → Webhooks*).  
- `FILE_PATH` → Path to the `.txt` file with video links (exported from the Chrome extension).  
- `DELAY_SEC` → Optional delay (in seconds) between messages to prevent rate-limit errors.  

3. **Save and close the file.**  

---

## ▶️ Usage

1. Export all links from your YouTube playlist with [YouTube URL Extractor](https://chromewebstore.google.com/detail/youtube-url-extractor/jmilibpbdpajjnabchfpfmmmjgbimefo).  
2. Save them into a `.txt` file (one link per line).  
3. Run the script:  

```bash
python links.py
```

4. The script will send all links to your Discord channel automatically.  

---

## 📂 Example

**Input file (`Links.txt`):**  
```
https://youtu.be/video1
https://youtu.be/video2
https://youtu.be/video3
```

**Discord Output (in channel):**  
```
https://youtu.be/video3
https://youtu.be/video2
https://youtu.be/video1
```

*(Reverse order ensures the first video stays at the top.)*  

---

## ⚠️ Notes

- Do not share your webhook URL publicly – anyone with it can post messages to your Discord channel.  
- Large playlists may take time to post (because of the delay).  
- If you hit **Discord rate limits**, increase the `DELAY_SEC` value.  

---

## 📜 License

This project is free to use and modify.  
