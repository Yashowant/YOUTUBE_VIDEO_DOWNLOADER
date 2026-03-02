# 🎬 YouTube Video Downloader (Python)

A simple Python-based YouTube video downloader built using **yt-dlp**.  
This tool allows you to download YouTube videos (including Shorts) directly to your local machine.

---

## 🚀 Features

- ✅ Download normal YouTube videos
- ✅ Download YouTube Shorts
- ✅ Automatically selects best available quality
- ✅ Saves files into a `downloads` folder
- ✅ Lightweight and easy to use

---

## 📦 Requirements

- Python 3.8+
- pip (Python package manager)

---

## 🔧 Installation

### 1️⃣ Clone or Download the Project

```bash
git clone <your-repo-url>
cd ytvideodownloader
```

Or just download and extract the folder.

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install yt-dlp
```

---

## ▶️ Usage

Run the script:

```bash
python ytpy.py
```

Enter the YouTube URL when prompted:

```
Enter YouTube URL: https://www.youtube.com/watch?v=example
```

The video will be downloaded into the `downloads` folder.

---

## 📁 Project Structure

```
ytvideodownloader/
│
├── ytpy.py
├── downloads/
└── README.md
```

---

## 🛠 Example Code

```python
import os
import yt_dlp

url = input("Enter YouTube URL: ")

if not os.path.exists("downloads"):
    os.makedirs("downloads")

ydl_opts = {
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'format': 'best'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completed!")
```

---

## ⚠ Disclaimer

This tool is for educational purposes only.  
Please respect YouTube’s Terms of Service and copyright laws when downloading content.

---

## 📌 Future Improvements (Optional Ideas)

- Download audio only (MP3)
- Add progress bar
- Build a GUI version
- Convert into standalone `.exe`
- Add quality selection option

---

Built using Python ❤️