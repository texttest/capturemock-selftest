#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import os, subprocess

    subprocess.call([ "python", "subproc.py" ])

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    

