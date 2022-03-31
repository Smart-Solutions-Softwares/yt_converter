from flask import Flask, render_template, request, redirect
import src.yt as yt
import threading
import logging

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/download', methods=['GET', 'POST'])
def my_form_post():
    if request.method == 'POST':
        yt_url = ''
        yt_url_raw = request.form['link']
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
        x = threading.Thread(target=yt.thread_delete_file, args=(f"static/{output[1]}/{output[0]}.{output[1]}",))
        x.start()
        return render_template('download.html', title=output[0], format=output[1])
    else:
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
