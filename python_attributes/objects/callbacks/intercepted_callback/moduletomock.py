
theCallback=None

class TheObject:
    def __init__(self):
        self.value = 0

    def setValue(self, ans):
        self.value = ans
        return "The answer"
        
def setCallback(callback):
    global theCallback
    theCallback = callback

def doStuffWithCallback(*args):
    return theCallback(*args) + " is "

