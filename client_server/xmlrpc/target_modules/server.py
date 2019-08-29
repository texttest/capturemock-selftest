#!/usr/bin/env python

import os, socket, sys, xmlrpc.server   

# Restrict to a particular path.
class RequestHandler(xmlrpc.server.SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 0), requestHandler=RequestHandler, logRequests=False)
server.register_introspection_functions()

# Register pow() function; this will use the value of
# pow.__name__ as the name, which is just 'pow'.
server.register_function(pow)

# Register a function under a different name
def adder_function(x,y):
    return x + y
server.register_function(adder_function, 'add')

def add_newlines(s):
    return s + "First Line\nExtra Line\nNew Extra Line"

server.register_function(add_newlines)

def a_stupidly_long_function_name_to_test_pprinting_in_mock_files():
    pass

server.register_function(a_stupidly_long_function_name_to_test_pprinting_in_mock_files)


host, port = server.socket.getsockname()
address = "http://" + host + ":" + str(port)
message = "Started mathematical server at " + address
print(message)
sys.stdout.flush()

# Run the server's main loop
server.serve_forever()
