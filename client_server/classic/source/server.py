#!/usr/bin/env python

from SocketServer import TCPServer, StreamRequestHandler
import sys, os, socket, time

def createSocket():
    servAddr = os.getenv("CAPTUREMOCK_SERVER")
    if servAddr:
        host, port = servAddr.split(":")
        serverAddress = (host, int(port))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(serverAddress)
        return sock

def sendServerState(stateDesc):
    sock = createSocket()
    if sock:
        sock.sendall("SUT_SERVER:" + stateDesc + "\n")
        sock.close()

class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        clientData = self.rfile.read()
        if clientData.strip() == "terminate":
            self.wfile.write("Exiting...")
            global gotExit
            gotExit = True
        elif not clientData.startswith("Don't answer"):
            self.wfile.write("Length was " + str(len(clientData)))

server = TCPServer(("localhost", 0), MyRequestHandler)
host, port = server.socket.getsockname()
address = host + ":" + str(port)
message = "Started string-length server at " + address
sendServerState(message)
time.sleep(0.1) # Prevent race conditions
# Not all server states set the server location. Make sure we remember this...
sendServerState("Nice day today!")
print message
sys.stdout.flush()

gotExit = False
while not gotExit:
    server.handle_request()
