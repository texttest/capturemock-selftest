#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError
import sys

@capturemock(rcFiles=["capturemockrc"])
def test():
    import packagetomock
    from packagetomock.mymodule import getObject
    print(getObject().getValue())


try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
