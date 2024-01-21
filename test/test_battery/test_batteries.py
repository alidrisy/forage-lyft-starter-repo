import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from service_able import Serviceable


class TeasNubbinBattery(unittest.TestCase):
    """Class to test the nubbin battry model"""
    def test_inhirtince(self):
        """test if NubbinBattery inhirt from Serviceable"""
        self.assertIsInstance(NubbinBattery, type(Serviceable))
    
    def test_needs_service(self):
        """test if NubbinBattery needs service after 4 yers"""
        last_date = datetime(2020, 1, 15)
        current_date = datetime.now()
        nubbin = NubbinBattery(last_date, current_date)
        self.assertTrue(nubbin.needs_service())

    def test_not_needs_service(self):
        """test if NubbinBattery need or not service after 3 years"""
        last_date = datetime(2021, 1, 15)
        current_date = datetime.now()
        nubbin = NubbinBattery(last_date, current_date)
        self.assertFalse(nubbin.needs_service())


class TeasSpindlerBattery(unittest.TestCase):
    """Class to test the SpindlerBattery model"""
    def test_inhirtince(self):
        """test if SpindlerBattery inhirt from Serviceable"""
        self.assertIsInstance(SpindlerBattery, type(Serviceable))
    
    def test_needs_service(self):
        """test if SpindlerBattery needs service after 2 yers"""
        last_date = datetime(2022, 1, 15)
        current_date = datetime.now()
        spindler = SpindlerBattery(last_date, current_date)
        self.assertTrue(spindler.needs_service())

    def test_not_needs_service(self):
        """test if SpindlerBattery need or not service after 1 years"""
        last_date = datetime(2023, 1, 15)
        current_date = datetime.now()
        spindler = SpindlerBattery(last_date, current_date)
        self.assertFalse(spindler.needs_service())


if __name__ == '__main__':
    unittest.main()
