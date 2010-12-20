#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import packagetomock.sub.moduletomock
    
    print packagetomock.sub.moduletomock.call_function() + " " + packagetomock.sub.moduletomock.attribute

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    
