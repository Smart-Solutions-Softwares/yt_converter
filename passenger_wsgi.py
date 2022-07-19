import sys, os
INTERP = os.path.join(os.environ['HOME'], 'ytmp3mp4.online', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())


sys.path.append('app')
from app.app import app as application

# import sys, os
# # INTERP = os.path.join(os.environ['HOME'], 'app.ytmp3mp4.online', 'bin', 'python3')
# INTERP = os.path.join(os.environ['HOME'], 'app.youtube-mp3-mp4.com', 'bin', 'python3')
# if sys.executable != INTERP:
#     os.execl(INTERP, INTERP, *sys.argv)
# sys.path.append(os.getcwd())
#
#
# from flask import Flask
# application = Flask(__name__)
#
#
#
# @application.route('/')
# def index():
#     return 'Hello Passenger'