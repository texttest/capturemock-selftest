#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    o = moduletomock.object
    print(o.getValue())
    print(moduletomock.callFunction(o, param=o))

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
