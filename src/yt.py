import os, re
import youtube_dl
import time

DELETE_DELAY = 600


def dl_yt(url, output):
    frmt = {'mp3': False, 'mp4': True}
    typ = {'mp3': 'audio', 'mp4': ''}
    y = {'nocheckcertificate': True}

    video_info = youtube_dl.YoutubeDL(y).extract_info(
        url=url, download=False)
    if not os.path.exists(f"static/{output}"):
        os.makedirs(f"static/{output}")
    revised_title = re.sub(r"[^a-zA-Z0-9 ]", "", video_info['title']).replace(" ", "_")
    filename = f"static/{output}/{revised_title}.{output}"
    options = {
        'format': f'best{typ[output]}',
        'keepvideo': frmt[output],
        'outtmpl': filename,
        'nocheckcertificate': True
    }
    youtube_dl.YoutubeDL(options).download([url])
    return revised_title, output


def thread_delete_file(file):
    time.sleep(DELETE_DELAY)
    try:
        os.remove(file)
    except (FileNotFoundError, IsADirectoryError):
        pass

