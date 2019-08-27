#!/usr/bin/env python

import subprocess, sys, os
subprocess.call([ sys.executable, "target_modules/client.py", os.getenv("CAPTUREMOCK_SERVER") ])
