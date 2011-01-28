#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"], mode=1)
def test():
    print "Hello world!"

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value))
    

