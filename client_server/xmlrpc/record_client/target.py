#!/usr/bin/env python

import os, sys, subprocess, signal, xmlrpc.client
from threading import Thread
from time import sleep

def sendServerState(address):
    servAddr = os.getenv("CAPTUREMOCK_SERVER")
    if servAddr:
        proxy = xmlrpc.client.ServerProxy(servAddr)
        proxy.setServerLocation(address)

def runClientThread():
    sleep(4) # give the server chance to start
    clientPath = os.path.join(os.getenv("TEXTTEST_SANDBOX"), "target_modules", "client.py")
    subprocess.call([ sys.executable, clientPath, os.getenv("CAPTUREMOCK_SERVER") ])

clientThread = Thread(target=runClientThread)
clientThread.start()
serverPath = os.path.join(os.getenv("TEXTTEST_SANDBOX"), "target_modules", "server.py")
serverProc = subprocess.Popen([ sys.executable, serverPath ], stdout=subprocess.PIPE, stderr=open(os.devnull, "w"), cwd=os.path.expanduser("~"))
serverAddress = serverProc.stdout.readline().strip().split()[-1]
sendServerState(serverAddress)
clientThread.join()
try:
    serverProc.terminate()
except:
    os.kill(serverProc.pid, signal.SIGTERM)

serverProc.wait()
