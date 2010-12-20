#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    print moduletomock.attribute
    print moduletomock.otherattribute
    print moduletomock.method()
    print moduletomock.othermethod()
    print moduletomock.ClassName.staticMethod()
    print moduletomock.ClassName.otherStaticMethod()
    print moduletomock.ClassName().otherStaticMethod()

    class MyClassName(moduletomock.OtherClassName):
        pass

    print MyClassName().method()

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    
