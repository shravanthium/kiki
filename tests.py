import unittest
from courier import Courier
from scheduler import Scheduler


class CourierTests(unittest.TestCase):
    def setUp(self):
        self.package_without_offer = Courier("PKG1", 100, 5, 5)
        self.package_with_offer = Courier("PKG1", 100, 10, 100, "OFR003")
        self.package1 = Courier("PKG1", 100, 50, 30, "OFR001")
        self.package2 = Courier("PKG2", 100, 75, 125, "OFFR0008")
        self.package3 = Courier("PKG3", 100, 175, 100, "OFFR003")
        self.package4 = Courier("PKG4", 100, 110, 60, "OFFR002")
        self.package5 = Courier("PKG5", 100, 155, 95, "NA")

        self.schedule1 = Scheduler(
            [self.package1, self.package2, self.package3, self.package4, self.package5],
            200,
            2,
            70,
        )
        self.schedule_packages1 = self.schedule1.get_shipment()
        self.schedule2 = Scheduler(
            [self.package1, self.package3, self.package5], 200, 2, 70
        )
        self.schedule_packages2 = self.schedule2.get_shipment()

    def test_delivery_cost(self):
        self.assertEqual(self.package_without_offer.delivery_cost(), 175)

    def test_discount(self):
        self.assertEqual(self.package_with_offer.discount(), 35)

    def test_total_cost(self):
        self.assertEqual(self.package_with_offer.total_cost(), 665)

    def test_get_shipment(self):
        self.assertEqual(
            sum([pkg.pkg_weight_in_kg for pkg in self.schedule_packages1]), 185
        )
        self.assertEqual(
            sum([pkg.pkg_weight_in_kg for pkg in self.schedule_packages2]), 175
        )

    def test_remaning_packages(self):
        self.assertEqual(len(self.schedule1.remaining_packages), 3)

    def test_updated_delivery_time(self):
        self.assertEqual(
            self.schedule1.update_delivery_time(self.schedule_packages1), 3.58
        )
    

if __name__ == "__main__":
    unittest.main()
