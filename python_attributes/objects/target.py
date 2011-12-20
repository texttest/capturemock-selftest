#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock

    obj = moduletomock.getObject("""Some Multiline
String""")
    if isinstance(obj, moduletomock.TheClass):
        if isinstance(obj, moduletomock.TheBaseClass):
            print(obj.getNumber() + 1)
            print("Nonsense attributes = " + repr(hasattr(obj, "nonsense")))
        else:
            print("Not the Base!")
    else:
        print("Not the Class!")


try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")

