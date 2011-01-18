#!/usr/bin/env python

import os

os.system("delete_editor " + os.path.abspath("file"))
os.system("delete_editor " + os.path.abspath("writedir"))
os.system("delete_editor no_such_file")
