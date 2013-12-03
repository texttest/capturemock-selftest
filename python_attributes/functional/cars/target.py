from capturemock import capturemock, RECORD, REPLAY

@capturemock('cars', mode=RECORD)
def test_cars():
    from cars import CarFactory, Car, Wheel

    car_factory = CarFactory()
    print(car_factory)

    car = car_factory.make_car()
    print(car)

    for wheel in car.wheels:
        assert isinstance(wheel, Wheel)
        assert wheel.size == 15
        print('wheel.id = %r' % wheel.id)

test_cars()
