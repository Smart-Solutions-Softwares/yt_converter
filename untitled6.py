# -*- coding: utf-8 -*-


from pytube import YouTube
import os

import requests

""" The first API """
""" Change the following link """
url = "https://youtube-to-mp32.p.rapidapi.com/api/yt_to_mp3"

""" If you are using API link , do not change the following  lines
But if you are using a youtube link ,uncomment from line 15 till 24 """
"""querystring = {"video_id":"edPREMPZ5RA"}

headers = {
    'x-rapidapi-host': "youtube-to-mp32.p.rapidapi.com",
    'x-rapidapi-key': "7fd28c8244msh192131f69ff095ep140a0ajsn0a5f135310eb"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()"""

""" The second API """

url2 = "https://youtube-to-mp34.p.rapidapi.com/metadata/P0PBuWFeTY4"

headers2 = {
    'x-rapidapi-host': "youtube-to-mp34.p.rapidapi.com",
    'x-rapidapi-key': "7fd28c8244msh192131f69ff095ep140a0ajsn0a5f135310eb"
    }

response2 = requests.request("GET", url2, headers=headers2)

data2 = response2.json()
#print(data2)

yt = YouTube(url)

try:
  print("Downloading.......")
  video = yt.streams.filter(only_audio=True).first()
  out_file = video.download()

  base, ext = os.path.splitext(out_file)

  new_file = base + '.mp3'
  os.rename(out_file, new_file)
  print("Successfully downloaded")

except:
  print(data2["message"])

