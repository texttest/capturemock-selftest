#!/usr/bin/env python

import os
from threading import Thread
from time import sleep

def runClientThread():
    sleep(4) # give the server chance to start
    os.system("client.py " + os.getenv("CAPTUREMOCK_SERVER") + " > " + os.devnull)

clientThread = Thread(target=runClientThread)
clientThread.start()
os.system("server.py")
