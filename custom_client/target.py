#!/usr/bin/env python

# We pretend we aren't working in Python, so we don't import capturemock

import os, socket

def sendText(text, serverAddress):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(serverAddress)
    sock.sendall(text.encode())
    return sock

def sendRecord(code, *args):
    import moduletomock
    sendText("SUT_CUSTOM:" + code + ":SUT_SEP:" + eval(code), *args)

def printReplay(code, *args):
    sock = sendText("SUT_CUSTOM:" + code, *args)
    sock.shutdown(1)
    print(sock.makefile().read())
    sock.close()

def getServerAddress():
    servAddr = os.getenv("CAPTUREMOCK_SERVER")
    host, port = servAddr.split(":")
    return host, int(port)

address = getServerAddress()
if os.getenv("CAPTUREMOCK_MODE") == "1":
    # record
    sendRecord("moduletomock.attribute", address)
    sendRecord("moduletomock.call_function('hello')", address)
else:
    # replay
    printReplay("moduletomock.attribute", address)
    printReplay("moduletomock.call_function('hello')", address)
