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
    moduletomock.setCallback(str)
    print("The answer is " + moduletomock.doStuffWithCallback(42))

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
