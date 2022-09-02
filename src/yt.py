import os
import re
import youtube_dl
import time
from datetime import datetime
from pytz import timezone
import logging
import threading

tz = timezone('US/Eastern')

DELETE_DELAY = 180
MAX_RETRY = 3


def dl_yt(url, output):
    datetime_started = datetime.now(tz)
    frmt = {'mp3': False, 'mp4': True}
    typ = {'mp3': 'audio', 'mp4': ''}
    y = {'nocheckcertificate': True}

    video_info = youtube_dl.YoutubeDL(y).extract_info(
        url=url, download=False)
    if not os.path.exists(f"static/{output}"):
        os.makedirs(f"static/{output}")
    revised_title1 = re.sub(r"[^a-zA-Z0-9 ]", "", video_info['title']).strip().replace(" ", "_")
    revised_title = re.sub(r"\_{2,}", "_", revised_title1)
    filename = f"static/{output}/{revised_title}.{output}"
    csv_file = f"static/{output}/{output}.csv"
    options = {
        'format': f'best{typ[output]}',
        'keepvideo': frmt[output],
        'outtmpl': filename,
        'nocheckcertificate': True
    }
    youtube_dl.YoutubeDL(options).download([url])
    f = open(csv_file, "a")
    f.write(f"{datetime_started},{datetime.now(tz)},{datetime.now(tz) - datetime_started},{output},{revised_title},{url}\n")
    f.close()
    x = threading.Thread(target=thread_delete_file, args=(f"static/{output}/{revised_title}.{output}",))
    x.start()
    return revised_title, output


def thread_delete_file(file):
    for x in range(MAX_RETRY):
        try:
            logging.info(f"==========Queued for Deletion at {datetime.now(tz)}: {file}===========")
            print(f"==========Queued for Deletion at {datetime.now(tz)}: {file}===========")
            time.sleep(DELETE_DELAY / (x + 1))
            logging.info(f"==========Deleting file at {datetime.now(tz)}: {file} after {x+1} try.===========")
            print(f"==========Deleting file at {datetime.now(tz)}: {file} after {x+1} try.===========")
            os.remove(file)
        except (FileNotFoundError, IsADirectoryError) as err:
            print(err)
            f2 = open("logs_thread.csv", "a")
            f2.write(f"{datetime.now(tz)},{file},{str(err)}\n")
            f2.close()

        logging.info(f"=========={file} has been deleted at {datetime.now(tz)} after {x+1} try.===========")
        print(f"=========={file} has been deleted at {datetime.now(tz)} after {x+1} try.===========")
        break
