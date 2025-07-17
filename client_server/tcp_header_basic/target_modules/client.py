#!/usr/bin/env python

import sys, socket

def runQuery(sock, toSend):
    sendBytes = (len(toSend) + 4).to_bytes(4) + toSend.encode()
    sock.send(sendBytes)
    print("Sent to server:", toSend)
    if toSend != "terminate":
        try:
            lengthBytes = sock.recv(4)
            length = int.from_bytes(lengthBytes)
            if length > 0:
                responseBytes = sock.recv(length - 4)
                response = responseBytes.decode()
                print("Got reply:", response)
        except TimeoutError:
            print("Timed out waiting for reply!")

servAddr = sys.argv[1]
host, port = servAddr.split(":")
serverAddress = (host, int(port))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serverAddress)
sock.settimeout(1)
runQuery(sock, "Here is a string")
runQuery(sock, "Here is a longer string\r\nwith a newline")
runQuery(sock, "Don't answer this one")
runQuery(sock, "terminate")
