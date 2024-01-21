import unittest

from tire.octoprime_tire import OctoprimeTire
from service_able import Serviceable


class TestOctoprimeTire(unittest.TestCase):
    """Class to test the OctoprimeTire model"""
    def test_inhirtince(self):
        """test if OctoprimeTire inhirt from Serviceable"""
        self.assertIsInstance(OctoprimeTire, type(Serviceable))
    
    def test_needs_service(self):
        """test if OctoprimeTire needs service the sum of all values in
        the tire wear array is greater than or equal to 3."""
        tires = [0.9, 0.5, 0.6, 1]
        octoprime = OctoprimeTire(tires)
        self.assertTrue(octoprime.needs_service())

    def test_not_needs_service(self):
        """test if OctoprimeTire need or not servicethe sum of all values in
        the tire wear array is not greater than or equal to 3"""
        tires = [0.4, 0.2, 0.3, 0.5]
        octoprime = OctoprimeTire(tires)
        self.assertFalse(octoprime.needs_service())


if __name__ == '__main__':
    unittest.main()
