#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    factory = moduletomock.MyFactory()
    print(factory.object.getAnswer())
    # Check we handle if it isn't cached
    print(factory.object.getAnswer())

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
