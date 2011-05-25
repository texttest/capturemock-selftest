
class MyObject:
    def getAnswer(self):
        return "Answer"

class MyFactory:
    def __getattr__(self, name):
        return MyObject()

