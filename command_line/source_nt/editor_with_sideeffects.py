#!/usr/bin/env python

import sys, os

def editFile(fileName):
    print "Editing file", os.path.basename(fileName)
    file = open(fileName, "a")
    file.write("The Editor has made its mark\n")

fileName = sys.argv[1]
editFile(fileName)
myPath = os.getenv("MY_PATH")
if myPath:
    editFile(os.path.join(myPath, "sideeffect"))
else:
    editFile("sideeffect")
