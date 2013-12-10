#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    obj = moduletomock.getInstance()
    print(obj.getValue())
    print(isinstance(obj, moduletomock.Instance))
    obj2 = obj.callback
    print(obj2.getValue())

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")

