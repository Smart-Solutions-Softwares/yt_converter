from flask import Flask, render_template, request
import src.yt as yt

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/download', methods=['POST'])
def my_form_post():
    yt_url = request.form['text']
    vid_format = request.form['format']
    yt.dl_yt(yt_url, vid_format)
    print("Download complete...")

    return "Downloaded Successfully"


if __name__ == "__main__":
    app.run(debug=True)
