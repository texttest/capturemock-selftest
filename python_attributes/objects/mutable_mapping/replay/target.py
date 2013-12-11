from capturemock import capturemock, REPLAY

@capturemock('moduletomock', mode=REPLAY)
def test():
    from moduletomock import MyDict

    mutable_mapping = MyDict(animal='dog')

    print('mutable_mapping["animal"] = %r' % mutable_mapping["animal"])

test()
