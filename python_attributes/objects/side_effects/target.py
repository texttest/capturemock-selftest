#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    theObject = moduletomock.MyObject()
    print(theObject.value)
    print(theObject.value)
    print(theObject.value)
    theObject.setValue("My Value")
    print(theObject.value)
    print(theObject.value)
    theObject.setValue("Final Value")
    print(theObject.value)
    print(theObject.value)
    print(theObject.value)

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
