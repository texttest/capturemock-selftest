#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    import indirectmodule
    
    print(moduletomock.getValue(1))
    print(indirectmodule.getValue(2))
    print(moduletomock.getValue(3))
    print(indirectmodule.getValue(4))

test()

