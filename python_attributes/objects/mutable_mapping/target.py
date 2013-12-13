from capturemock import capturemock

@capturemock('moduletomock')
def test():
    from moduletomock import MyDict

    mutable_mapping = MyDict(animal='dog')

    print('mutable_mapping["animal"] = %r' % mutable_mapping["animal"])

test()
