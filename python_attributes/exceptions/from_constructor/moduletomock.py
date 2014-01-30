
class MyObject:
    instance = None
    def __init__(self):
        if self.instance:
            raise RuntimeError, "Not allowed to construct these!"
        else:
            MyObject.instance = self
