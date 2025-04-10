#!/usr/bin/env python

import socket, time

def send_data(conn_sock, field, value):
    sendBytes = b""
    for item in [ 16, 1, field, value ]:
        sendBytes += item.to_bytes(4)
    conn_sock.send(sendBytes)
    print("Sent to server:", field, value)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 0))
sock.listen(2)

host, port = sock.getsockname()
address = host + ":" + str(port)
message = "Started string-length server at " + address
print(message, flush=True)
connSocket, _ = sock.accept()
time.sleep(0.3)
send_data(connSocket, 1, 1)
time.sleep(0.3)
send_data(connSocket, 2, 0)
