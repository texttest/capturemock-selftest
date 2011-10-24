
class Base:
    def __init__(self, value):
        self.value = value
    def getValue(self):
        return self.value
    
class MyNewObject(Base, object):
    def getOverrideValue(self):
        return "New Style!"

class MyObject(Base):
    def getOverrideValue(self):
        return "Old Style!"

    def doNothing(self):
        pass
