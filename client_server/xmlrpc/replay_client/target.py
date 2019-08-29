#!/usr/bin/env python

import subprocess, sys, os
clientPath = os.path.join(os.getenv("TEXTTEST_SANDBOX"), "target_modules", "client.py")
subprocess.call([ sys.executable, clientPath, os.getenv("CAPTUREMOCK_SERVER") ])
