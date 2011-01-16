#!/usr/bin/env python

import os

os.mkdir("tmpdir")
os.chdir("tmpdir")
os.system("editor_with_sideeffects " + os.path.abspath("file"))
