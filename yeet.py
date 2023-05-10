import os
import youtube_dl
import vlc
import time
import playsound
from playsound import playsound
media_player = vlc.MediaPlayer()
with open("music.txt", "r") as f:
    da = f.read().splitlines()
    print(da[0])
    ydl_opts = {
        'format': 'bestaudio/best',
        'default_search': 'ytsearch',
        'noplaylist': True,
        'quiet': True,
        'postprocessors': [{
           'key': 'FFmpegExtractAudio',
           'preferredcodec': 'mp3',
           'preferredquality': '149000'
       }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([da[0]])
    for file in os.listdir():             #Add the directory here
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    time.sleep(3)
    playsound("song.mp3")