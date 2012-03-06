#!/usr/bin/env python

import os, subprocess, signal, xmlrpclib
from threading import Thread
from time import sleep

def sendServerState(address):
    servAddr = os.getenv("CAPTUREMOCK_SERVER")
    if servAddr:
        proxy = xmlrpclib.ServerProxy(servAddr)
        proxy.setServerLocation(address)

serverProc = subprocess.Popen([ "server.py" ], stdout=subprocess.PIPE, shell=True)
serverAddress = serverProc.stdout.readline().strip().split()[-1]
sendServerState(serverAddress)
try:
    serverProc.terminate() # needs python2.6
except:
    os.kill(serverProc.pid, signal.SIGTERM) # needs posix
serverProc.wait()
