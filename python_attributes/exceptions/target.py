#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock, sys
    try:
        import no_such_module
    except ImportError, e:
        print "Caught exception:", e

    try:
        print moduletomock.no_such_method("argument", faking=True)
    except Exception, e:
        print "Caught exception:", e

    try:
        # invalid arguments
        print moduletomock.call_function("argument", faking=True)
    except Exception, e:
        print "Caught exception:", e

    import urllib2
    try:
        print urllib2.urlopen("foo://no.such.site")
    except urllib2.URLError, e:
        print "Caught exception:", e.args[0]

    try:
        print urllib2.urlopen("foo://another.no.such.site")
    except EnvironmentError:
        from traceback import format_exception_only
        exc_type, exc_value = sys.exc_info()[:2]
        print "".join(format_exception_only(exc_type, exc_value))

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
