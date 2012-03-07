#!/usr/bin/env python

import xmlrpclib, sys

servAddr = sys.argv[1]
s = xmlrpclib.ServerProxy(servAddr)
val = s.pow(2,3)  # Returns 2**3 = 8
print val  
print s.add(val,3)  # Returns 11
print s.add_newlines("") # test empty strings...
try:
    print s.no_such_method("str")
except xmlrpclib.Fault, e:
    print "Caught exception for missing method..."
    print str(e)
# Print list of available methods
print s.system.listMethods()
