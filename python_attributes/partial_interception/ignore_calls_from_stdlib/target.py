#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import logging, os, sys

    logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(message)s")
    logging.info("My process ID is " + str(os.getpid()) + "\n")

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    
