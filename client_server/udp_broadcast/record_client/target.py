#!/usr/bin/env python

import os, subprocess, sys, socket, signal
from threading import Thread
from time import sleep
from urllib.request import urlopen
from locale import getpreferredencoding

def sendServerAddress(address):
    print("send", address, flush=True)
    servAddr = os.getenv("CAPTUREMOCK_SERVER")
    if servAddr:
        host, port = servAddr.split(":")
        serverAddress = (host, int(port))
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(serverAddress)
        sock.sendall(b"SUT_SERVER:" + address.replace(b"0.0.0.0", b"localhost") + b"\n")
        sock.close()

def runClientThread():
    sleep(4) # give the server chance to start
    subprocess.call([ sys.executable, "target_modules/client.py", os.getenv("CAPTUREMOCK_SERVER") ])

clientThread = Thread(target=runClientThread)
clientThread.start()
serverPath = os.path.join(os.getenv("TEXTTEST_SANDBOX"), "target_modules", "server.py")
serverProc = subprocess.Popen([ sys.executable, serverPath ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=os.path.expanduser("~"))
serverAddress = serverProc.stdout.readline().strip().split()[-1]
sendServerAddress(serverAddress)
clientThread.join()
serverProc.terminate()
#os.kill(serverProc.pid, signal.SIGTERM)

serverProc.wait()
