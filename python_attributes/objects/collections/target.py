#!/usr/bin/env python

from capturemock import capturemock

@capturemock(rcFiles=["capturemockrc"])
def test():
    import moduletomock
    for name, animal in moduletomock.get_named_animals().items():
        print name, "says", animal.speak()

    animal1, animal2 = moduletomock.get_animal_tuple()
    print animal1.sizeCompare(animal2)

    myDog = moduletomock.Dog()
    if myDog.inPack([ animal1, animal2, myDog ]):
        print "My dog is in the pack"

    try:
        animalList = moduletomock.get_animals()
        print animalList
        for animal in animalList:
            print animal.milk() + " the " + type(animal).__name__ + "..."
    except moduletomock.BadAnimal, e:
        print "BadAnimal Exception:", e


try:
    test()
except:
    import sys; sys.stderr.write(str(sys.exc_value) + "\n")
