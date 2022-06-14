import sys, os
INTERP = os.path.join(os.environ['HOME'], 'ytmp3mp4_app', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())


sys.path.append('ytmp3mp4_app')
from ytmp3mp4_app.app import app as application

