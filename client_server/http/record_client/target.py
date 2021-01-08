#!/usr/bin/env python

import os, subprocess, sys
from threading import Thread
from time import sleep
from urllib.request import urlopen

def sendServerAddress(address):
    servAddr = os.getenv("CAPTUREMOCK_SERVER")
    if servAddr:
        url = servAddr + "/capturemock/setServerLocation"
        urlopen(url, data=address).read()

def runClientThread():
    sleep(4) # give the server chance to start
    subprocess.call([ sys.executable, "target_modules/client.py", os.getenv("CAPTUREMOCK_SERVER") ])

clientThread = Thread(target=runClientThread)
clientThread.start()
serverPath = os.path.join(os.getenv("TEXTTEST_SANDBOX"), "target_modules", "server.py")
serverProc = subprocess.Popen([ sys.executable, serverPath ], stdout=subprocess.PIPE, stderr=open(os.devnull, "w"), cwd=os.path.expanduser("~"))
serverAddress = serverProc.stdout.readline().strip().split()[-1]
sendServerAddress(serverAddress)
clientThread.join()
try:
    serverProc.terminate()
except:
    os.kill(serverProc.pid, signal.SIGTERM)

serverProc.wait()


