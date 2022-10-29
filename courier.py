""" 
Courier: This module contains courier class with methods to compute cost to deliver packages.
"""

class Courier():

    def __init__(self, base_delivery_cost, pkg_weight_in_kg, distance_in_km):
        self.base_delivery_cost = base_delivery_cost
        self.pkg_weight_in_kg = pkg_weight_in_kg
        self.distance_in_km = distance_in_km

    def delivery_cost(self):
        #DELIVERY COST=Base Delivery Cost+(Package Total Weight * 10)+(Distance to Destination * 5)

        return self.base_delivery_cost + (self.pkg_weight_in_kg * 10) + (self.distance_in_km * 5)