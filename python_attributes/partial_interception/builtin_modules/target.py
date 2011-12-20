#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import datetime

    print("Today is " + str(datetime.date.today()))
    print("Another date was " + str(datetime.date(2010, 1, 1)))


try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
