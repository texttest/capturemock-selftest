#!/usr/bin/env python

import subprocess, sys, os
from urllib.request import urlopen
from locale import getpreferredencoding
import capturemock

serverPath = os.path.join(os.getenv("TEXTTEST_SANDBOX"), "target_modules", "server.py")
serverProc = subprocess.Popen([ sys.executable, serverPath ], stdout=subprocess.PIPE, stderr=open(os.devnull, "w"), cwd=os.path.expanduser("~"))
serverAddress = str(serverProc.stdout.readline().strip().split()[-1], getpreferredencoding())
args = sys.argv[1:] + [ serverAddress ]
capturemock.replay_for_server(*args)
try:
    serverProc.terminate()
except:
    os.kill(serverProc.pid, signal.SIGTERM)

serverProc.wait()


