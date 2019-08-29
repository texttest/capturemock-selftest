#!/usr/bin/env python

import os, subprocess, signal, xmlrpc.client, sys
from threading import Thread
from time import sleep

def sendServerState(address):
    servAddr = os.getenv("CAPTUREMOCK_SERVER")
    if servAddr:
        proxy = xmlrpc.client.ServerProxy(servAddr)
        proxy.setServerLocation(address)

serverPath = os.path.join(os.getenv("TEXTTEST_SANDBOX"), "target_modules", "server.py")
serverProc = subprocess.Popen([ sys.executable, serverPath ], stdout=subprocess.PIPE, stderr=open(os.devnull, "w"), cwd=os.path.expanduser("~"))
serverAddress = serverProc.stdout.readline().strip().split()[-1]
sendServerState(serverAddress)
try:
    serverProc.terminate() # needs python2.6
except:
    os.kill(serverProc.pid, signal.SIGTERM) # needs posix
serverProc.wait()
