#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock("packagetomock")
def test():
    import packagetomock.sub.moduletomock
    
    print(packagetomock.sub.moduletomock.call_function() + " " + packagetomock.sub.moduletomock.attribute)

@capturemock("packagetomock")
def test2():
    import packagetomock.sub.moduletomock
    
    print(packagetomock.sub.moduletomock.attribute + " " + packagetomock.sub.moduletomock.call_function())

try:
    test()
    test2()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
