#!/usr/bin/env python

import os, sys
print("In syscalls.py now")
sys.stdout.flush()

exitStatus = os.system('firstcall -a -b -c "hello | goodbye"')
if os.name == "posix":
    exitStatus = os.WEXITSTATUS(exitStatus)
print("firstcall exited with status", exitStatus)
sys.stdout.flush()
