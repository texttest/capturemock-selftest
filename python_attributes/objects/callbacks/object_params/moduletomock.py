
class MyObject:
    def __init__(self, callback):
        self.callback = callback
        self.value = None

    def doStuffWithCallback(self):
        self.value = "Callback used"
        return "Returned and " + self.callback(self)

theObject = None

def setCallback(callback):
    global theObject
    theObject = MyObject(callback)

def doStuffWithCallback():
    return theObject.doStuffWithCallback()
