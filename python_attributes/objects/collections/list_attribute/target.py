from capturemock import capturemock, RECORD, REPLAY

@capturemock('moduletomock', mode=RECORD)
def test():
    import moduletomock

    for wheel in moduletomock.wheels:
        print('wheel.id = %r' % wheel.id)

test()
