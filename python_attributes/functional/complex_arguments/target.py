#!/usr/bin/env python

from capturemock import capturemock
import sys

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock

    strVal = """This
is a large unicode string"""
    if sys.version_info[0] == 2:
        strVal = unicode(strVal)

    withQuote = """This one
has a ' in it"""

    windowsPath = "C:\\no_such_directory"

    print(moduletomock.call_function({ "string" : strVal,
                                       "quotestring": withQuote,
                                       "windows_path": windowsPath }))


try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
