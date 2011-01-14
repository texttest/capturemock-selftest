#!/usr/bin/env python

import os, sys
print "In syscalls.py now"
sys.stdout.flush()

exitStatus = os.system('firstcall -a -b -c "hello | goodbye"')
if os.name == "posix":
    exitStatus = os.WEXITSTATUS(exitStatus)
print "firstcall exited with status", exitStatus
sys.stdout.flush()

# Repeat the first command again, it might cause problems (!)
os.system('firstcall -a -b -c "hello | goodbye"')

# Check our environment and current working directory goes into the traffic environment
os.environ["MY_ENV_VAR"] = "value"
os.environ["PATH"] = "/some/extra/path" + os.pathsep + os.getenv("PATH")
del os.environ["MY_ENV_FOR_UNSET"]
os.mkdir("tmpdir")
os.chdir("tmpdir")
os.system("secondcall -c -x")
