#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import packagetomock
    
    obj = packagetomock.getObject()
    newObj = obj.construct(packagetomock.sub.TheClass)
    print newObj.getValue()

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    
