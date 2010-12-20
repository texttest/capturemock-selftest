#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    try:
        moduletomock.callFunction()
    except Exception, e:
        print "Caught exception", e
    
try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    

