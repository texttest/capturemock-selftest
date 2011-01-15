#!/usr/bin/env python

import subprocess, os
subprocess.call([ "firstcall", "arg1", "arg2", "arg3" ])
subprocess.call([ "firstcall", "arg2", "arg1", "arg3" ])
subprocess.call([ "firstcall", "arg1", "arg2", "arg3" ])
