#!/usr/bin/env python

import xmlrpc.client, sys

servAddr = sys.argv[1]
s = xmlrpc.client.ServerProxy(servAddr)
val = s.pow(2,3)  # Returns 2**3 = 8
print(val)
val2 = s.pow(3,2) # Returns 3**2 = 9
print(val2)
print(s.add(val,val2))  # Returns 17
print(s.add_newlines("")) # test empty strings...
try:
    print(s.no_such_method("str"))
except xmlrpc.client.Fault as e:
    print("Caught exception for missing method...")
    print(str(e))
# Print list of available methods
print(s.system.listMethods())
