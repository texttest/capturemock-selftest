#!/usr/bin/env python

# ordinarily would be in some initialisation file
from capturemock import process_startup
process_startup()
import moduletomock
    
print(moduletomock.call_function())
