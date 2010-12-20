#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    import indirectmodule
    
    print moduletomock.getValue(1)
    print indirectmodule.getValue(2)
    print moduletomock.getValue(3)
    print indirectmodule.getValue(4)
    try:
        import moduletomock2
    except ImportError:
        print "Failed to import bad module as expected"

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    

