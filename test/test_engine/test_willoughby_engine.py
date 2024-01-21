import unittest

from engine.willoughby_engine import WilloughbyEngine
from service_able import Serviceable


class TestWilloughbyEngine(unittest.TestCase):
    """Class to test the WilloughbyEngine model"""
    def test_inhirtince(self):
        """test if WilloughbyEngine inhirt from Serviceable"""
        self.assertIsInstance(WilloughbyEngine, type(Serviceable))
    
    def test_needs_service(self):
        """test if WilloughbyEngine needs service after 60000 miles"""
        last_mileage = 30000
        current_maileage = 91000
        willoughby = WilloughbyEngine(current_maileage, last_mileage)
        self.assertTrue(willoughby.needs_service())

    def test_not_needs_service(self):
        """test if WilloughbyEngine need or not service after 50000 miles"""
        last_mileage = 30000
        current_maileage = 80000
        willoughby = WilloughbyEngine(current_maileage, last_mileage)
        self.assertFalse(willoughby.needs_service())


if __name__ == '__main__':
    unittest.main()
