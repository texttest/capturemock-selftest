
callbacks = []

def addCallbacks(arg, *args):
    global callbacks
    callbacks += args

def doStuffWithCallback():
    for callback in callbacks:
        callback()

def getCallbackPostfix():
    return "Postfix!"
