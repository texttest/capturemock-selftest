#!/usr/bin/env python

import sys
from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import os, subprocess

    subprocess.call([ sys.executable, "subproc.py" ])

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    

