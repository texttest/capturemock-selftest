#!/usr/bin/env python

from capturemock import capturemock
import mysystem

@capturemock("moduletomock")
def test():
    mysystem.dostuff()

test()
    
