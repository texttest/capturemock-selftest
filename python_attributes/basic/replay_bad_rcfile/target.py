#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["no_such_file", "capturemockrc"])
def test():
    import moduletomock
    import smtplib # for testing additional filtering

    print moduletomock.call_function() + " " + moduletomock.attribute

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    
