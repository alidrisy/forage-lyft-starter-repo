import unittest
from datetime import datetime

from battery.spindler_battery import SpindlerBattery
from service_able import Serviceable


class TestSpindlerBattery(unittest.TestCase):
    """Class to test the SpindlerBattery model"""
    def test_inhirtince(self):
        """test if SpindlerBattery inhirt from Serviceable"""
        self.assertIsInstance(SpindlerBattery, type(Serviceable))
    
    def test_needs_service(self):
        """test if SpindlerBattery needs service after 3 yers"""
        today = datetime.today().date()
        last_date = today.replace(year=today.year - 4)
        current_date = datetime.today().date()
        spindler = SpindlerBattery(last_date, current_date)
        self.assertTrue(spindler.needs_service())

    def test_not_needs_service(self):
        """test if SpindlerBattery need or not service after 2 years"""
        today = datetime.today().date()
        last_date = today.replace(year=today.year - 2)
        current_date = datetime.today().date()
        spindler = SpindlerBattery(last_date, current_date)
        self.assertFalse(spindler.needs_service())


if __name__ == '__main__':
    unittest.main()
