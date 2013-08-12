#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    
    x = moduletomock.Zero()
    if not x:
        print "Zero was zero!"

    x = moduletomock.LenZero()
    if not x:
        print "LenZero was zero!"

    x = moduletomock.Normal()
    if x:
        print "Normal was normal!"

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")

