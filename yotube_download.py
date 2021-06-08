import youtube_dl

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(['https://www.youtube.com/watch?v=qDMCZ1Fv7WA']) # 주소를 [] 안에 넣기