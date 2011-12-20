#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    dates = moduletomock.get_dates()
    gap = dates["finished"] - dates["started"]
    print(str(gap.days) + " days")

test()

