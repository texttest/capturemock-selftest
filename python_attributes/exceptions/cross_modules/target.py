#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    try:
        moduletomock.callFunction()
    except Exception as e:
        print("Caught exception " + str(e))
    
try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    

