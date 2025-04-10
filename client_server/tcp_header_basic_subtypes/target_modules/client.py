#!/usr/bin/env python

import sys, socket

def readValue(sock):
    try:
        lengthBytes = sock.recv(8)
        length = int.from_bytes(lengthBytes[:4])
        if length > 0:
            msgType = int.from_bytes(lengthBytes[4:])
            responseBytes = sock.recv(length - 8)
            subType = int.from_bytes(responseBytes[:4])
            value = int.from_bytes(responseBytes[4:])
            print("Got reply:", msgType, subType, value)
    except TimeoutError:
        print("Timed out waiting for reply!")

servAddr = sys.argv[1]
host, port = servAddr.split(":")
serverAddress = (host, int(port))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serverAddress)
sock.settimeout(0.4) # too fast for the default capturemock timeout
readValue(sock)
readValue(sock)
