

class Instance:
    def __init__(self):
        self.callback = Callback()

    def getValue(self):
        return 42

class Callback:
    def getValue(self):
        return 58


def getInstance():
    return Instance()

