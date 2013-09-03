#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    class CallbackClass:
        def callback(self):
            print("In callback! " + moduletomock.getCallbackPostfix())

    def callback2():
        print("In callback2! " + moduletomock.getCallbackPostfix())

    cc = CallbackClass()
    moduletomock.addCallbacks("argument", cc.callback, callback2)
    moduletomock.addCallbacks("argument", cc.callback, callback2)
    print(moduletomock.doStuffWithCallback())

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
