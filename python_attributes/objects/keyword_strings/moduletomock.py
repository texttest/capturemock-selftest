
from pprint import pformat

class MyObject:
    def __init__(self):
        self.kw = {}

    def setData(self, **kw):
        self.kw = kw

    def getDescription(self):
        return pformat(self.kw)
