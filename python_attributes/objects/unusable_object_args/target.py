#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    class Difficult:
        def __repr__(self):
            return "<You'll never evaluate me!>"

    d1 = Difficult()
    d2 = Difficult()

    print moduletomock.callFunction(d1, param=d2)

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")

