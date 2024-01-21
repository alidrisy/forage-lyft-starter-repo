import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from service_able import Serviceable


class TeasCapuletEngine(unittest.TestCase):
    """Class to test the CapuletEngine model"""
    def test_inhirtince(self):
        """test if NubbinBattery inhirt from Serviceable"""
        self.assertIsInstance(CapuletEngine, type(Serviceable))
    
    def test_needs_service(self):
        """test if NubbinBattery needs service after 30000 miles"""
        last_mileage = 30000
        current_maileage = 61000
        capulet = CapuletEngine(current_maileage, last_mileage)
        self.assertTrue(capulet.needs_service())

    def test_not_needs_service(self):
        """test if NubbinBattery need or not service after 25000 miles"""
        last_mileage = 30000
        current_maileage = 50000
        capulet = CapuletEngine(current_maileage, last_mileage)
        self.assertFalse(capulet.needs_service())


class TeasWilloughbyEngine(unittest.TestCase):
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

    
class TeasSternmanEngine(unittest.TestCase):
    """Class to test the SternmanEngine model"""
    def test_inhirtince(self):
        """test if SternmanEngine inhirt from Serviceable"""
        self.assertIsInstance(SternmanEngine, type(Serviceable))
    
    def test_needs_service(self):
        """test if SternmanEngine needs service after 60000 miles"""
        warning_light_is_on = True
        sternman = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman.needs_service())

    def test_not_needs_service(self):
        """test if SternmanEngine need or not service after 50000 miles"""
        warning_light_is_on = False
        sternman = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman.needs_service())


if __name__ == '__main__':
    unittest.main()
    