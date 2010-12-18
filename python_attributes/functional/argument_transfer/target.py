#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    
    print moduletomock.callFunction("hello", 1, None, third=0.3, second=2, first=None) 

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value))
    

