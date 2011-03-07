#!/usr/bin/env python

from capturemock import capturemock, RECORD

@capturemock("socket", mode=RECORD)
def test():
    import socket
    
    print socket.gethostname()

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value))
    

