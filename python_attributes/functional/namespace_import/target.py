#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    from moduletomock import *
    
    print call_function() + " " + attribute

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    
