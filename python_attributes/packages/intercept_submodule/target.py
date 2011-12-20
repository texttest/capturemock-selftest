#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    from packagetomock.moduletomock import call_module_function, module_attribute
    print(call_module_function("arg"))
    print(module_attribute)
    
    import packagetomock
    print(packagetomock.call_package_function("arg2"))
    print(packagetomock.package_attribute)

try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_info()[1]) + "\n")
    
