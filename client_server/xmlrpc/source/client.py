#!/usr/bin/env python

import xmlrpclib, sys

servAddr = sys.argv[1]
s = xmlrpclib.ServerProxy(servAddr)
print s.pow(2,3)  # Returns 2**3 = 8
print s.add(2,3)  # Returns 5
try:
    print s.no_such_method("str")
except xmlrpclib.Fault, e:
    print "Caught exception for missing method..."
    print str(e)
# Print list of available methods
print s.system.listMethods()
