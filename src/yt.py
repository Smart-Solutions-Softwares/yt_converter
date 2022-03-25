import os, re
import youtube_dl


def dl_yt(url, output):
    frmt = {'mp3': False, 'mp4': True}
    typ = {'mp3': 'audio', 'mp4': ''}
    y = {'nocheckcertificate': True}

    video_info = youtube_dl.YoutubeDL(y).extract_info(
        url=url, download=False)
    if not os.path.exists(output):
        os.makedirs(output)
    revised_title = re.sub(r"[^a-zA-Z0-9 ]", "", video_info['title']).replace(" ", "_")
    filename = f"{output}/{revised_title}.{output}"
    options = {
        'format': f'best{typ[output]}',
        'keepvideo': frmt[output],
        'outtmpl': filename,
        'nocheckcertificate': True
    }

    return youtube_dl.YoutubeDL(options).download([url])
