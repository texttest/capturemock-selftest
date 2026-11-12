#!/usr/bin/env python

import os, time

os.system("editor.py file")
time.sleep(2) # let the asynchronous edit of "file" happen before the next command
os.system("editor.py file2")
time.sleep(3)
