#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    gap = moduletomock.get_date1() - moduletomock.get_date2()
    print gap.days, "days"

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    
