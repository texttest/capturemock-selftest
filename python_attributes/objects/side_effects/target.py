#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    theObject = moduletomock.MyObject()
    print(theObject.value)
    print(theObject.value)
    theObject.setValue("My Value")
    print(theObject.value)

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
