from playsound import playsound
import youtube_dl
from youtube_dl import YoutubeDL
import os
import vlc
import time
os.system("clear")
media = vlc.MediaPlayer("test.mp3")
queue = []
for file in os.listdir("./"):
    if file.endswith(".mp3"):
        os.remove(file)
hehe = input("Queue or play one song?\n")
if hehe.lower() == "queue":
     queue1 = input("What songs do you wanna add? If you are done with choosing songs then type 'done'\n")
     queue.append(queue1)
     while True:
         try:
            queue1 = input("Gonna add more songs to the queue?\n")
            queue.append(queue1)
            if queue1.lower() == "done":
                queue.pop(-1)
                print(queue)
                print("Okay gonna start playing audio")
                ydl_opts = {
                    'quiet': True,
                    'format': 'bestaudio/best',
                    'default_search': 'ytsearch',
                    'noplaylist': True,
                    'no_warnings': True,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '149000'
                    }]
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([queue[int(0)]])
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "test.mp3")
                while True:
                    print(f"Playing: {queue[int(0)]}")
                    playsound("test.mp3")
                    del(queue[int(0)])
                    while playsound.is_playing():
                        time.sleep(1)
                    else:
                        for file in os.listdir("./"):
                            if file.endswith("test.mp3"):
                                os.remove(file)
         except Exception:
            print(Exception)
             
if hehe.lower() == "play":
    queue2 = input("What song do you wanna play?\n")
    ydl_opts = {
     'format': 'bestaudio/best',
     'default_search': 'ytsearch',
     'noplaylist': True,
     'no_warnings': True,
     'postprocessors':[{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '149000'
     }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     ydl.download([queue2])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
         os.rename(file, "test.mp3")
    playsound("test.mp3")