
class Zero(object):
    # Python 2.x
    def __nonzero__(self):
        return False

    # Python 3.x
    def __bool__(self):
        return False

class LenZero(object):
    def __len__(self):
        return 0

class Normal(object):
    pass

