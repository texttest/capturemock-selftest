#!/usr/bin/env python

from capturemock import capturemock

@capturemock("moduletomock")
def test():
    import moduletomock

    return moduletomock.call_function() + " " + moduletomock.attribute

try:
    print test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    
