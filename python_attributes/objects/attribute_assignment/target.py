#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    theObject = moduletomock.MyObject()
    theObject.value = "My Value"
    theObject.itself = theObject
    print theObject.itself.getValue()

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    
