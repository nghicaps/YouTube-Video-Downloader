#get Pytube from pip (Python package installer)
from pytube import YouTube
from sys import argv
#get ffmpeg for audio and video muxing (optional, for the higher res videos)
import ffmpeg
import os

# link has to be the second argument
link = argv[1]
yt = YouTube(link)

# output title and views of video
title = yt.title
print("Title: ", title)
views = '{:,}'.format(yt.views)
print("Views: ", views)

# find top audio file for download
res = ''
for stream in yt.streams.filter(adaptive=True, audio_codec = 'mp4a.40.2'):
    
    if stream.resolution != res:
        print(stream.resolution)
    res = stream.resolution
    stream.download('C:/Users/phamh/Desktop', filename='audio.mp4')
    print("audio downloaded")
    break

# find video file with best resolution for download
# higher res videos (1080p and up) most likely do not have audio mixed in
for stream in yt.streams.filter(adaptive=True, file_extension='mp4'):
    
    if stream.resolution != res:
        print(stream.resolution)
    res = stream.resolution
    stream.download('C:/Users/phamh/Desktop', filename='video.mp4')
    print("video downloaded")
    break

# make sure both audio and video files exist in folder
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

find('audio.mp4', 'C:/Users/phamh/Desktop')
print("audio found")
find('video.mp4', 'C:/Users/phamh/Desktop')
print("video found")

# make sure filename is unused in folder
path = "C:\\Users\\phamh\\Desktop\\" + title + ".mp4"

if os.path.exists(path):
    title = title + "(1)"
    print("\"" + path + "\"" + " already exists, adding to filename")

print("new filename: " + title + ".mp4")

# audio and video muxing
audio_stream = ffmpeg.input('audio.mp4')
video_stream = ffmpeg.input('video.mp4')
print("starting muxing")
ffmpeg.output(audio_stream, video_stream, title + '.mp4').run()
print("audio and video combined")

# delete unnecessary separate audio and video files
os.remove('audio.mp4')
print("audio file deleted")
os.remove('video.mp4')
print("video file deleted")

print("enjoy your new video")
