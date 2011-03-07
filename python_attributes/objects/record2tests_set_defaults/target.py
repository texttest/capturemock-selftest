#!/usr/bin/env python

from capturemock import capturemock, set_defaults, CaptureMockReplayError

set_defaults(rcFiles=["capturemockrc"])

class TestClass:
    @capturemock
    def test(self):
        import moduletomock

        obj = moduletomock.getObject("name")
        print obj.getNumber() + 1
    
    @capturemock
    def test2(self):
        import moduletomock
        
        obj = moduletomock.getObject("name2")
        print obj.getNumber() + 2
    

try:
    x = TestClass()
    x.test()
    x.test2()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")

