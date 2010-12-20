
class MyObject:
    def getValue(self):
        pass

    def getFunctionAnswer(self):
        return "Answer"
    
def callFunction(obj, param=None):
    return param.getFunctionAnswer()

object = MyObject()
