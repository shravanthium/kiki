import unittest
from courier import Courier

class CourierTests(unittest.TestCase):

    def test_compute_delivery_cost(self):
        package = Courier(100,5,5)
        self.assertEqual(package.delivery_cost(), 175)


if __name__ == '__main__':
    unittest.main()