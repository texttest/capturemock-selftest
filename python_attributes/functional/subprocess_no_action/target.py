#!/usr/bin/env python

import sys
from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import os, subprocess, sys
    import moduletomock
    
    print(moduletomock.call_function() + " " + moduletomock.attribute)
    sys.stdout.flush()

    subprocess.call([ sys.executable, "subproc.py" ])

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    

