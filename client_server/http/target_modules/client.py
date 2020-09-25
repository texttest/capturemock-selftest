#!/usr/bin/env python

import sys, socket
from locale import getpreferredencoding
from urllib.request import urlopen

def runQuery(url, toSend=None):
    print("Sending to url", url)
    print("Sent to server:", toSend, flush=True)
    try:
        response = str(urlopen(url, data=toSend).read(), "utf-8")
        print("Got reply:", response, flush=True)
    except Exception as e:
        print("FAILED! ", str(e))

serverAddress = sys.argv[1]
if not serverAddress.startswith("http://"):
    serverAddress = "http://" + serverAddress
runQuery(serverAddress + "/strings", b"Here is a string")
runQuery(serverAddress + "/strings", b"Here is a longer string")
runQuery(serverAddress + "/bad/path", b"Don't answer this one")
runQuery(serverAddress + "/terminate")
