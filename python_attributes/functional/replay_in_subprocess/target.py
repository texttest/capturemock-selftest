#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import os, subprocess

    pyfile = os.path.join(os.getenv("TEXTTEST_ROOT"), "target.py")
    subprocess.call([ "python", pyfile ])

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    

