from pytube import YouTube
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context
link="https://www.youtube.com/watch?v=kffacxfA7G4"
path="/Users/shahoreertalha/Desktop/Desktop/Work/TheBro Music/song draft"
vd=YouTube(link)
vd.streams.get_lowest_resolution().download(path)