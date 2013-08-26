#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    theObject = moduletomock.object
    print(theObject.getDescription())

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
