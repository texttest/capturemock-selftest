#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    theObj = moduletomock.TheObject()
    moduletomock.setCallback(theObj.setValue)
    prefix = moduletomock.doStuffWithCallback(42)
    print(prefix + str(theObj.value))

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
