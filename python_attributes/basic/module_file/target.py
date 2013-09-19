#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock("moduletomock")
def test():
    import moduletomock

    print("File is " + moduletomock.__file__)

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
