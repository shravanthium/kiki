import unittest
from courier import Courier

class CourierTests(unittest.TestCase):

    def test_delivery_cost(self):
        package = Courier(100,5,5)
        self.assertEqual(package.delivery_cost(), 175)
    
    def test_discount(self):
        package = Courier(100,10,100,"OFR003")
        self.assertEqual(package.discount(), 35)


if __name__ == '__main__':
    unittest.main()