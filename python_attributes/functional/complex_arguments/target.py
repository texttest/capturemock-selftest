#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock

    strVal = u"""This
is a large unicode string"""

    withQuote = """This one
has a ' in it"""

    windowsPath = "C:\\no_such_directory"

    print moduletomock.call_function({ "string" : strVal,
                                       "quotestring": withQuote,
                                       "windows_path": windowsPath })


try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
    
