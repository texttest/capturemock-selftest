#!/usr/bin/env python

import subprocess, sys, os
from urllib.request import urlopen

def sendServerAddress(address):
    servAddr = os.getenv("CAPTUREMOCK_SERVER")
    if servAddr:
        url = servAddr + "/capturemock/setServerLocation"
        urlopen(url, data=address).read()

serverPath = os.path.join(os.getenv("TEXTTEST_SANDBOX"), "target_modules", "server.py")
serverProc = subprocess.Popen([ sys.executable, serverPath ], stdout=subprocess.PIPE, stderr=open(os.devnull, "w"), cwd=os.path.expanduser("~"))
serverAddress = serverProc.stdout.readline().strip().split()[-1]
sendServerAddress(serverAddress)
try:
    serverProc.terminate()
except:
    os.kill(serverProc.pid, signal.SIGTERM)

serverProc.wait()


