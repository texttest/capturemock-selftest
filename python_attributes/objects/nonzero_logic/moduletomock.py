
class Zero(object):
    def __nonzero__(self):
        return False

class LenZero(object):
    def __len__(self):
        return 0

class Normal(object):
    pass

