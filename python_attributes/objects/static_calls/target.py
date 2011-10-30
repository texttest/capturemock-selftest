#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock

    print moduletomock.TheClass.attribute
    print moduletomock.TheClass.getNumber()

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")

