
theCallback=None

def setCallback(callback):
    global theCallback
    theCallback = callback

def doStuffWithCallback(*args):
    return theCallback(*args)
