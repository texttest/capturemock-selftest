#!/usr/bin/env python

# Most command-line tools write non-ASCII text in the locale's encoding. Show what the system under test receives
import locale, subprocess
encoding = locale.getencoding() if hasattr(locale, "getencoding") else locale.getpreferredencoding(False)
proc = subprocess.run([ "secondcall", "Größe" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("secondcall wrote", ascii(proc.stderr.decode(encoding).splitlines()[0]))
