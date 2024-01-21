import unittest
from datetime import datetime

from service_able import Serviceable
from car_factory import CarFactory
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery



class TestCarFactory(unittest.TestCase):
    """Class to test the CarFactory model"""

    def test_is_car(self):
        """Test the return value of the model CarFactory is Car"""
        last_service_date = datetime(2020, 12, 15)
        current_date = datetime.now()
        calliope = CarFactory.create_calliope(current_date, last_service_date, 40000, 32000)
        self.assertIsInstance(calliope, Car)
        
    def test_is_theright_battery(self):
        """Test the return value of the model CarFactory is Car with
        the right battery (calliopeCar with spindlerBattery)"""
        last_service_date = datetime(2020, 12, 15)
        current_date = datetime.now()
        calliope = CarFactory.create_calliope(current_date, last_service_date, 40000, 32000)
        self.assertIsInstance(calliope.battery, SpindlerBattery)

    def test_is_theright_engine(self):
        """Test the return value of the model CarFactory is Car with
        the right engine (calliopeCar with capulitEngine)"""
        last_service_date = datetime(2020, 12, 15)
        current_date = datetime.now()
        calliope = CarFactory.create_calliope(current_date, last_service_date, 40000, 32000)
        self.assertIsInstance(calliope.engine, CapuletEngine)


class TestCalliope(unittest.TestCase):
    """Test the calliope car"""
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_date = datetime.today().date()
        warning_light_is_on = False

        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_date = datetime.today().date()
        warning_light_is_on = False

        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        warning_light_is_on = True

        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        warning_light_is_on = False

        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
