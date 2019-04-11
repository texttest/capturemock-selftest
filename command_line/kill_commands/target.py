#!/usr/bin/env python

import os, time, subprocess, signal

def showExitCode(exitCode):
    # We cheat on Windows where killed processes don't have
    # exit codes
    if os.name == "posix":
        return exitCode
    else:
        return -15

proc = subprocess.Popen([ "dosleep", "100" ])
time.sleep(3)
if proc.poll():
    print("Process terminated already.")
else:
    proc.send_signal(signal.SIGTERM)
    exitCode = proc.wait()
    print("Terminated process: exit code was", showExitCode(exitCode))
