from car_factory import CarFactory
import datetime

last = datetime.datetime(2021, 12, 15)
cur = datetime.datetime.now()
calliope = CarFactory.create_calliope(cur, last, 40000, 32000, [0, 1, 1, 1])
b = calliope.battery
print(calliope.needs_service())
