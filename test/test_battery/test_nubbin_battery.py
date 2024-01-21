import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from service_able import Serviceable


class TestNubbinBattery(unittest.TestCase):
    """Class to test the NubbinBattery model"""
    def test_inhirtince(self):
        """test if NubbinBattery inhirt from Serviceable"""
        self.assertIsInstance(NubbinBattery, type(Serviceable))
    
    def test_needs_service(self):
        """test if NubbinBattery needs service after 4 yers"""
        today = datetime.today().date()
        last_date = today.replace(year=today.year - 4)
        current_date = datetime.today().date()
        nubbin = NubbinBattery(last_date, current_date)
        self.assertTrue(nubbin.needs_service())

    def test_not_needs_service(self):
        """test if NubbinBattery need or not service after 3 years"""
        today = datetime.today().date()
        last_date = today.replace(year=today.year - 3)
        current_date = datetime.today().date()
        nubbin = NubbinBattery(last_date, current_date)
        self.assertFalse(nubbin.needs_service())


if __name__ == '__main__':
    unittest.main()
