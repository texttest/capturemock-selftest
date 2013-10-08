#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock

    obj = moduletomock.getObject("name")
    print(obj.getNumber() + 1)
    

@capturemock(rcFiles=["capturemockrc"])
def test2():
    import moduletomock

    obj = moduletomock.getObject("name")
    print(obj.getNumber() + 2)
    

try:
    test()
    test2()
except:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")

