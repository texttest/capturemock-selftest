#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock

    obj = moduletomock.getObject("""Some Multiline
String""")
    if isinstance(obj, moduletomock.TheClass) and \
           isinstance(obj, moduletomock.TheBaseClass):
        print obj.getNumber() + 1
        print "Nonsense attributes = " + repr(hasattr(obj, "nonsense"))
    else:
        print "Strange type here!"


try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")

