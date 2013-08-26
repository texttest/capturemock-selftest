
class MyIntObject(int):
    def getDescription(self):
        return "The answer is " + str(self)

object = MyIntObject(42)
