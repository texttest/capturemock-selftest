

class MyIterator(object):
    def __init__(self, l):
        self.otheriter = l

    def next(self):
        return self.otheriter.next()

class MyList(list):
    def __iter__(self):
        return MyIterator(list.__iter__(self))
