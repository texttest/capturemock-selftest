#!/usr/bin/env python

# Some command-line tools write UTF-8 whatever the locale. capturemockrc says so for utf8call
import subprocess
proc = subprocess.run([ "utf8call", "Größe", "ō" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("utf8call wrote", ascii(proc.stdout.decode("utf-8").splitlines()[0]))
