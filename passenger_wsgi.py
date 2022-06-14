import sys, os
INTERP = os.path.join(os.environ['HOME'], 'ytmp3mp4_app2', 'bin', 'python')

if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())


sys.path.append('ytmp3mp4_app2')
from ytmp3mp4_app2.app import app as application

