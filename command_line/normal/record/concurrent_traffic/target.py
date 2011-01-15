#!/usr/bin/env python

import os, time
from threading import Thread

def run():
    os.system("dosleep 2")

x = Thread(target=run)
x.start()
time.sleep(0.5)
os.system("dosleep 0.5")
