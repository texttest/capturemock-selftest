#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def logtest():
    import logging
    import smtplib # for testing additional filtering

    print logging.getLevelName(50) + " " + str(logging.CRITICAL)

try:
    logtest()
except:
    import sys; sys.stderr.write(str(sys.exc_value))
    
