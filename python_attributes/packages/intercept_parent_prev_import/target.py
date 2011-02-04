#!/usr/bin/env python

from capturemock import capturemock
import mysystem

@capturemock("packagetomock", mode=1)
def test():
    mysystem.dostuff()

test()

