#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import logging, os, sys

    logging.basicConfig(level=logging.WARNING, stream=sys.stdout, format="%(message)s")
    logging.warn("My process ID is " + str(os.getpid()) + "\n")

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    

