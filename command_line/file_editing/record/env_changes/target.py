#!/usr/bin/env python

import os

os.mkdir("tmpdir")
os.environ["MY_PATH"] = "My path is " + os.path.abspath("tmpdir")
os.system("editor_with_sideeffects " + os.path.abspath("file"))
