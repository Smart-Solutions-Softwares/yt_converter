from flask import Flask, render_template, request, redirect
import src.yt as yt
import threading
import logging
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
        try:
            yt_url = ''
            yt_url_raw = request.form['link'].strip()
            f = open("logs.csv", "a")
            f.write(f"{datetime.now(tz)},{yt_url_raw}\n")
            if 'shorts' in yt_url_raw:
                yt_vid_id = yt_url_raw.split("/shorts/")[1]
                print(yt_vid_id)
                yt_url = f"https://www.youtube.com/watch?v={yt_vid_id}"
            elif '&' in yt_url_raw:
                yt_url = yt_url_raw.split("&")[0]
            else:
                yt_url = yt_url_raw
            vid_format = request.form['format']
            output = yt.dl_yt(yt_url, vid_format)
            logging.info("Download complete...")
            x = threading.Thread(target=thread_delete_file, args=(f"static/{output}/{revised_title}.{output}",))
            x.start()
            return render_template('download.html', title=output[0], format=output[1])
        except Exception as err:
            logging.info("SANDY LOGS:" + str(err))
            f = open("logs.csv", "a")
            f.write(f"{datetime.now(tz)},{yt_url_raw},{str(err)}\n")
            f.close()
            return redirect('/')
        f.close()
    else:
        return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
