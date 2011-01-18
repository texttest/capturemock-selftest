#!/usr/bin/env python

import os

os.system("editor.py " + os.path.abspath("file"))
os.system("editor.py " + os.path.abspath("writedir"))
os.system("editor.py no_such_file")
