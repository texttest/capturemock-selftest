#!/usr/bin/env python

from capturemock import capturemock
from capturemock.config import RECORD_ONLY_MODE

@capturemock("socket", mode=RECORD_ONLY_MODE)
def test():
    import socket
    
    print socket.gethostname()

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value))
    
