#!/usr/bin/env python

from capturemock import capturemock

@capturemock("moduletomock")
def test():
    import moduletomock

    print(moduletomock.call_function() + " " + moduletomock.attribute)

try:
    test()
    print(test.__name__)
except:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
