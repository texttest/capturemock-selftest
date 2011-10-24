#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    class MyDerived(moduletomock.MyObject):
        def getOverrideValue(self):
            return "Overridden!"

    class MyNewDerived(moduletomock.MyNewObject):
        def getOverrideValue(self):
            return "Overridden!"

    theObject = MyDerived("My Value")
    print theObject.getValue()
    print theObject.getOverrideValue()
    print isinstance(theObject, moduletomock.Base)

    theObject = MyNewDerived("My Value")
    print theObject.getValue()
    print theObject.getOverrideValue()
    print isinstance(theObject, moduletomock.Base)

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    
