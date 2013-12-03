class Wheel(object):
    size = 15

    def __init__(self, id):
        self.id = id

class Car(object):
    wheels = [
        Wheel(id=1),
        Wheel(id=2),
        Wheel(id=3),
        Wheel(id=4),
    ]

class CarFactory(object):
    def make_car(self):
        return Car()
