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

clientThread = Thread(target=runClientThread)
clientThread.start()
serverProc = subprocess.Popen([ "server.py" ], stdout=subprocess.PIPE, shell=True)
serverAddress = serverProc.stdout.readline().strip().split()[-1]
sendServerState(serverAddress)
clientThread.join()
try:
    serverProc.terminate()
except:
    os.kill(serverProc.pid, signal.SIGTERM)

serverProc.wait()
