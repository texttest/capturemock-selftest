
import sub

class MyObject(object):
    def construct(self, cls):
        return cls()

def getObject():
    return MyObject()
