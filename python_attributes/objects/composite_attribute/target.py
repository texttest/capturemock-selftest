#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    print moduletomock.object.hello + " world"

    # Do it twice and make sure it doesn't get recorded twice...
    print moduletomock.object.hello + " world"

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
