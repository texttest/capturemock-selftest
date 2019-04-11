#!/usr/bin/env python

import os, subprocess, signal, xmlrpc.client
from threading import Thread
from time import sleep

def sendServerState(address):
    servAddr = os.getenv("CAPTUREMOCK_SERVER")
    if servAddr:
        proxy = xmlrpc.client.ServerProxy(servAddr)
        proxy.setServerLocation(address)

def getServerArgs():
    for dir in os.getenv("PATH").split(os.pathsep):
        path = os.path.join(dir, "server.py")
        if os.path.isfile(path):
            return [ "python", path ]

serverProc = subprocess.Popen(getServerArgs(), stdout=subprocess.PIPE, stderr=open(os.devnull, "w"), cwd=os.path.expanduser("~"))
serverAddress = serverProc.stdout.readline().strip().split()[-1]
sendServerState(serverAddress)
try:
    serverProc.terminate() # needs python2.6
except:
    os.kill(serverProc.pid, signal.SIGTERM) # needs posix
serverProc.wait()
