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