
class TheBaseClass:
    pass

class TheClass(TheBaseClass):
    def getNumber(self):
        return 0

def getObject(*args):
    return TheClass()
