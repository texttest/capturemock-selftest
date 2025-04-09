#!/usr/bin/env python

import socket

def handle_requests(conn_sock):
    gotExit = False
    while True:
        lengthBytes = conn_sock.recv(4)
        if lengthBytes == 0:
            print("Timeout, exiting")
            return
        length = int.from_bytes(lengthBytes)
        msgBytes = conn_sock.recv(length - 4)
        msg = msgBytes.decode()
        print("Got message", msg)
        if msg == "terminate":
            print("Exiting...")
            return
        elif not msg.startswith("Don't answer"):
            answer = "Length was " + str(len(msg))
            answerBytes = (len(answer) + 4).to_bytes(4) + answer.encode()
            conn_sock.send(answerBytes)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 0))
sock.listen(2)

host, port = sock.getsockname()
address = host + ":" + str(port)
message = "Started string-length server at " + address
print(message, flush=True)
connSocket, _ = sock.accept()
connSocket.settimeout(10)

handle_requests(connSocket)
