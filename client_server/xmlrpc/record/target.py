#!/usr/bin/env python

import os, subprocess, signal, xmlrpclib
from threading import Thread
from time import sleep

def sendServerState(address):
    servAddr = os.getenv("CAPTUREMOCK_SERVER")
    if servAddr:
        proxy = xmlrpclib.ServerProxy(servAddr)
        proxy.setServerLocation(address)

def runClientThread():
    sleep(4) # give the server chance to start
    os.system("client.py " + os.getenv("CAPTUREMOCK_SERVER"))

def getServerArgs():
    for dir in os.getenv("PATH").split(os.pathsep):
        path = os.path.join(dir, "server.py")
        if os.path.isfile(path):
            return [ "python", path ]

clientThread = Thread(target=runClientThread)
clientThread.start()
serverProc = subprocess.Popen(getServerArgs(), stdout=subprocess.PIPE, stderr=open(os.devnull, "w"), cwd=os.path.expanduser("~"))
serverAddress = serverProc.stdout.readline().strip().split()[-1]
sendServerState(serverAddress)
clientThread.join()
try:
    serverProc.terminate()
except:
    os.kill(serverProc.pid, signal.SIGTERM)

serverProc.wait()
