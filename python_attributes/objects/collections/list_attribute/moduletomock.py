
class Wheel(object):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return "Wheel " + str(self.id)

wheels = [ Wheel(id=1), Wheel(id=2) ]
