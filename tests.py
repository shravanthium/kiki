import unittest
from courier import Courier
from scheduler import Scheduler


class CourierTests(unittest.TestCase):
    def test_delivery_cost(self):
        package = Courier("PKG1", 100, 5, 5)
        self.assertEqual(package.delivery_cost(), 175)

    def test_discount(self):
        package = Courier("PKG1", 100, 10, 100, "OFR003")
        self.assertEqual(package.discount(), 35)

    def test_total_cost(self):
        package = Courier("PKG1", 100, 10, 100, "OFR003")
        self.assertEqual(package.total_cost(), 665)

    def test_get_shipment(self):
        package1 = Courier("PKG1", 100, 50, 30, "OFR001")
        package2 = Courier("PKG2", 100, 75, 125, "OFFR0008")
        package3 = Courier("PKG3", 100, 175, 100, "OFFR003")
        package4 = Courier("PKG4", 100, 110, 60, "OFFR002")
        package5 = Courier("PKG5", 100, 155, 95, "NA")

        schedule1 = Scheduler(
            [package1, package2, package3, package4, package5], 200, 2, 70
        )
        schedule_packages1 = schedule1.get_shipment()
        self.assertEqual(sum([pkg.pkg_weight_in_kg for pkg in schedule_packages1]), 185)
        self.assertEqual(len(schedule1.remaining_packages), 3)
        self.assertEqual(schedule1.update_delivery_time(schedule_packages1), 3.58)

        schedule2 = Scheduler([package1, package3, package5], 200, 2, 70)
        schedule_packages2 = schedule2.get_shipment()
        self.assertEqual(sum([pkg.pkg_weight_in_kg for pkg in schedule_packages2]), 175)


if __name__ == "__main__":
    unittest.main()
