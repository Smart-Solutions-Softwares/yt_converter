from flask import Flask, render_template, request, redirect
import src.yt as yt

import threading
import logging
import re
from datetime import datetime
from pytz import timezone
tz = timezone('US/Eastern')

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/download', methods=['GET', 'POST'])
def my_form_post():
    if request.method == 'POST':
        f = open("logs.csv", "a")
        for x in range(yt.MAX_RETRY):
            try:
                yt_url_format = ['(http|https):\/\/[a-zA-Z0-9.]+\/watch\?v=([a-zA-Z0-9\_\-]+)[^a-zA-Z0-9_\-]*',
                                 '(http|https):\/\/[a-zA-Z0-9.]+\/shorts\/([a-zA-Z0-9\_\-]+)[^a-zA-Z0-9_\-]*',
                                 '(http|https):\/\/[a-zA-Z0-9.]+\/([a-zA-Z0-9\_\-]+)[^a-zA-Z0-9_\-]*']
                yt_url = ''
                yt_url_raw = request.form['link'].strip()
                for i in yt_url_format:
                    match = re.match(i, yt_url_raw)
                    if match:
                        yt_vid_id = match.group(2)
                        yt_url = f"https://www.youtube.com/watch?v={yt_vid_id}"
                        break
                vid_format = request.form['format']
                output = yt.dl_yt(yt_url, vid_format)
                logging.info("Download complete...")
                print("Download complete...")
                f.write(f"{datetime.now(tz)},{yt_url_raw},{yt_url},{output}\n")
                f.close()
                return render_template('download.html', title=output[0], format=output[1])
            except Exception as err:
                logging.info("SANDY LOGS:" + str(err))
                f.write(f"{datetime.now(tz)},{yt_url_raw},{yt_url},{str(err)}\n")
        f.close()
        x = threading.Thread(target=yt.thread_delete_file, args=(f"static/{output}/{output[0]}.{output[1]}.part",))
        x.start()
        return redirect('/')
    else:
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
