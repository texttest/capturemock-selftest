#!/usr/bin/env python

from capturemock import capturemock

@capturemock("socket")
def test():
    print "Hello world!"

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value))
    

