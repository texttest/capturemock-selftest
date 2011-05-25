#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    factory = moduletomock.MyFactory()
    print factory.object.getAnswer()
    # Check we handle if it isn't cached
    print factory.object.getAnswer()

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
