from flask import Flask, render_template, request, redirect
import src.yt as yt
import threading
import logging

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/download', methods=['POST'])
def my_form_post():
    yt_url = request.form['link']
    vid_format = request.form['format']

    if len(yt_url) > 0 and len(vid_format) > 0:
        output = yt.dl_yt(yt_url, vid_format)
        logging.info("Download complete...")
        x = threading.Thread(target=yt.thread_delete_file, args=(f"static/{output[1]}/{output[0]}.{output[1]}",))
        x.start()
        return render_template('download.html', title=output[0], format=output[1])
    else:
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
