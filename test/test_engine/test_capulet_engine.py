import unittest

from engine.capulet_engine import CapuletEngine
from service_able import Serviceable


class TestCapuletEngine(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
