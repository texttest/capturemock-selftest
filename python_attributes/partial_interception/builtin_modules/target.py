#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import datetime

    print "Today is", datetime.date.today()
    print "Another date was", datetime.date(2010, 1, 1)


try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    
