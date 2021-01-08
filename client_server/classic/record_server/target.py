#!/usr/bin/env python

import os, subprocess, sys
from threading import Thread
from time import sleep

def runClientThread():
    sleep(4) # give the server chance to start
    subprocess.call([ sys.executable, "target_modules/client.py", os.getenv("CAPTUREMOCK_SERVER") ], stdout=open(os.devnull, "w"))

clientThread = Thread(target=runClientThread)
clientThread.start()
subprocess.call([ sys.executable, "target_modules/server.py"])
