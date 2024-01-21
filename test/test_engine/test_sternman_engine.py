import unittest

from engine.sternman_engine import SternmanEngine
from service_able import Serviceable


class TestSternmanEngine(unittest.TestCase):
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
