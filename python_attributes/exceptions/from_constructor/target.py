#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError, RECORD

@capturemock(rcFiles=["capturemockrc"]) #, mode=RECORD)
def test():
    import moduletomock
    try:
        obj1 = moduletomock.MyObject()
        obj2 = moduletomock.MyObject()
    except RuntimeError as e:
        print("Caught exception: " + str(e))


try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
