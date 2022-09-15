from flask import Flask, render_template, request, redirect
from src.yt import convert_yt

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
        try:
            x = threading.Thread(target=convert_yt, args=(request.form['link'].strip(), request.form['format']))
            x.start()
            # output = convert_yt(request.form['link'].strip(), request.form['format'])
            return render_template('download.html', title=output[0], format=output[1])
        except:
            return redirect('/')
    else:
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
