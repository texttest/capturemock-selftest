
class MyObject:
    def __init__(self):
        self.callback = None
        self.value = None

    def setCallback(self, callback):
        self.callback = callback

    def doStuffWithCallback(self):
        self.value = "Callback used"
        return "Returned and " + self.callback(self)
