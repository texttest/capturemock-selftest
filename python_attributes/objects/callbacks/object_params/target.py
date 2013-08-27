#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

def callback(obj):
    print("In callback!")
    print(obj.value)
    print("Leaving callback")
    return "Finished"

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    moduletomock.setCallback(callback)
    print(moduletomock.doStuffWithCallback())

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
