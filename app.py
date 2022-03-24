from flask import Flask, render_template, request
import youtube_dl

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/download', methods=['POST'])
def my_form_post():
    yt_url = request.form['text']
    y = {'nocheckcertificate': True}

    video_info = youtube_dl.YoutubeDL(y).extract_info(
        url=yt_url, download=False)
    mp3_filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': mp3_filename,
        'nocheckcertificate': True
    }

    youtube_dl.YoutubeDL(options).download([yt_url])

    print("Download complete...")

    return "Downloaded Successfully"


if __name__ == "__main__":
    app.run(debug=True)
