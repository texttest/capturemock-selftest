#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import packagetomock
    
    print(packagetomock.getObject().getValue())


try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
