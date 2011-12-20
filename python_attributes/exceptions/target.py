#!/usr/bin/env python

from capturemock import capturemock, CaptureMockReplayError

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock, sys
    try:
        import no_such_module
    except ImportError as e:
        print("Caught exception: " + str(e))

    try:
        print(moduletomock.no_such_method("argument", faking=True))
    except Exception as e:
        print("Caught exception: " + str(e))

    try:
        # invalid arguments
        print(moduletomock.call_function("argument", faking=True))
    except Exception as e:
        print("Caught exception: " + str(e))

    import fakeurllib
    try:
        print(fakeurllib.urlopen("foo://no.such.site"))
    except fakeurllib.URLError as e:
        print("Caught exception: " + e.args[0])

    try:
        print(fakeurllib.urlopen("foo://another.no.such.site"))
    except EnvironmentError:
        from traceback import format_exception_only
        exc_type, exc_value = sys.exc_info()[:2]
        print("".join(format_exception_only(exc_type, exc_value)))

try:
    test()
except CaptureMockReplayError:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
