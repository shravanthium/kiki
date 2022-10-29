""" 
Courier: This module contains courier class with methods to compute cost to deliver packages.
"""


class Courier:
    valid_offers = {
        "OFR001": {
            "percent": 10,
            "distance": (0, 200),
            "weight": (70, 200),
        },
        "OFR002": {
            "percent": 7,
            "distance": (50, 150),
            "weight": (100, 250),
        },
        "OFR003": {
            "percent": 5,
            "distance": (50, 250),
            "weight": (10, 150),
        },
    }

    def __init__(self, base_delivery_cost, pkg_weight_in_kg, distance_in_km, offer_code=0):
        self.base_delivery_cost = base_delivery_cost
        self.pkg_weight_in_kg = pkg_weight_in_kg
        self.distance_in_km = distance_in_km
        self.offer_code = offer_code

    def delivery_cost(self):
        # DELIVERY COST=Base Delivery Cost+(Package Total Weight * 10)+(Distance to Destination * 5)

        return (
            self.base_delivery_cost
            + (self.pkg_weight_in_kg * 10)
            + (self.distance_in_km * 5)
        )

    def discount(self):
        if self.offer_code not in self.valid_offers.keys():
            return 0

        for offer, criteria in self.valid_offers.items():
            percent, distance, weight = (
                criteria["percent"],
                criteria["weight"],
                criteria["weight"],
            )

            if self.offer_code == offer:
                if self.distance_in_km in range(
                    distance[0], distance[1]
                ) and self.pkg_weight_in_kg in range(weight[0], weight[1]):
                    return (percent/100) * self.delivery_cost()

        return 0

    def total_cost(self):
        return self.delivery_cost() - self.discount()