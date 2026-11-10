#!/usr/bin/env python

import sys

# Write UTF-8 whatever the locale, as many tools do
sys.stdout.buffer.write(("utf8call called with " + repr(sys.argv[1:]) + "\n").encode("utf-8"))
