#!/usr/bin/env python

import packagetomock.moduletomock as mtm

def dostuff():
    print mtm.call_function() + " " + mtm.attribute

