#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    print(moduletomock.ClassName.staticMethod())
    print(moduletomock.ClassName.otherStaticMethod())
    obj = moduletomock.ClassName()
    print(obj.otherStaticMethod())
    print(obj.method())
    print(isinstance(obj, moduletomock.OtherClassName))

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
