#!/usr/bin/env python

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import os, socket, sys, xmlrpclib   

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer((socket.gethostname(), 0), requestHandler=RequestHandler, logRequests=False)
server.register_introspection_functions()

# Register pow() function; this will use the value of
# pow.__name__ as the name, which is just 'pow'.
server.register_function(pow)

# Register a function under a different name
def adder_function(x,y):
    return x + y
server.register_function(adder_function, 'add')

host, port = server.socket.getsockname()
address = "http://" + host + ":" + str(port)
message = "Started mathematical server at " + address
print message
sys.stdout.flush()

# Run the server's main loop
server.serve_forever()