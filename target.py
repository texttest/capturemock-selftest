#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    import smtplib # for testing additional filtering

    print moduletomock.call_function() + " " + moduletomock.attribute

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    