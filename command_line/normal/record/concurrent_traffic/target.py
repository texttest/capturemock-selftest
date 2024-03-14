#!/usr/bin/env python

import os, time
from threading import Thread

def run():
    os.system("dosleep 3")

x = Thread(target=run)
x.start()
time.sleep(1)
os.system("dosleep 1")
