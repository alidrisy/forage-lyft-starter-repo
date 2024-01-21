import unittest

from tire.carrigan_tire import CarriganTire
from service_able import Serviceable


class TestCarriganTire(unittest.TestCase):
    """Class to test the CarriganTire model"""
    def test_inhirtince(self):
        """test if CarriganTire inhirt from Serviceable"""
        self.assertIsInstance(CarriganTire, type(Serviceable))
    
    def test_needs_service(self):
        """test if CarriganTire needs service one or more of the
        values in the tire wear array is greater than or equal to 0.9"""
        tires = [0.9, 0.2, 0.3, 0.5]
        carrigan = CarriganTire(tires)
        self.assertTrue(carrigan.needs_service())

    def test_not_needs_service(self):
        """test if CarriganTire need or not service no 
        values in the tire wear array is greater than or equal to 0.9"""
        tires = [0.4, 0.2, 0.3, 0.5]
        carrigan = CarriganTire(tires)
        self.assertFalse(carrigan.needs_service())


if __name__ == '__main__':
    unittest.main()
