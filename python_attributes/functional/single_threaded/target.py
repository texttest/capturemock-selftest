#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock

    print "We used", moduletomock.threadCount(), "threads in this program"

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value))
    
