#!/usr/bin/env python

import os, subprocess, sys, io
from threading import Thread
from time import sleep
from urllib.request import urlopen
from locale import getpreferredencoding
from ftplib import FTP

def sendServerAddress(address):
    servAddr = os.getenv("CAPTUREMOCK_SERVER")
    if servAddr:
        host, port = servAddr.split(":")
        with FTP() as ftp:
            ftp.connect(host, int(port))
            ftp.login("capturemock", "capturemock")
            with io.BytesIO(b"") as f:
                ftp.storbinary("STOR SUT_SERVER=" + address.decode(), f)

def runClientThread():
    sleep(4) # give the server chance to start
    subprocess.call([ sys.executable, "target_modules/client.py", os.getenv("CAPTUREMOCK_SERVER") ])

clientThread = Thread(target=runClientThread)
clientThread.start()
serverPath = os.path.join(os.getenv("TEXTTEST_SANDBOX"), "target_modules", "server.py")

os.mkdir("ftp_server_dir")
with open("ftp_server_dir/README.txt", "w") as f:
    print("The data", file=f)
serverProc = subprocess.Popen([ sys.executable, serverPath ], stdout=subprocess.PIPE, stderr=open("server_errors.cpmock", "w"), cwd=os.path.abspath("ftp_server_dir"))
serverAddress = serverProc.stdout.readline().strip().split()[-1]
print("Server", serverAddress)
sendServerAddress(serverAddress)
clientThread.join()
output, _ = serverProc.communicate()
try:
    serverProc.terminate()
except:
    os.kill(serverProc.pid, signal.SIGTERM)

serverProc.wait()


