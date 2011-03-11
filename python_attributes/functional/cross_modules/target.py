#!/usr/bin/env python

from capturemock import capturemock, RECORD

@capturemock(["moduletomock", "moduletomock2"], mode=RECORD)
def test():
    import moduletomock2
    import moduletomock

    print moduletomock.attribute, moduletomock.call_function()
    
try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    

