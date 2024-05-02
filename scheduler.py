""" 
Scheduler: This module contains methods to compute estimated delivery time for each package.
"""

class Scheduler:
    def __init__(self, packages, max_load_capacity, available_trucks, max_speed):
        self.packages = packages
        self.max_load_capacity = max_load_capacity
        self.available_trucks = available_trucks
        self.remaining_packages = packages
        self.remaining_trucks = available_trucks
        self.max_speed = max_speed
        self.current_time = 0

    def get_shipment(self, remaining_packages, remaining_trucks):
        if not remaining_packages or remaining_trucks == 0:
            return []

        best_shipment = []
        best_shipment_weight = 0

        for i in range(len(remaining_packages)):
            current_shipment = []
            current_shipment_weight = 0
            for j in range(i, len(remaining_packages)):
                if current_shipment_weight + remaining_packages[j].pkg_weight_in_kg <= self.max_load_capacity:
                    current_shipment.append(remaining_packages[j])
                    current_shipment_weight += remaining_packages[j].pkg_weight_in_kg
            if current_shipment_weight > best_shipment_weight:
                best_shipment = current_shipment
                best_shipment_weight = current_shipment_weight

        return best_shipment

    def update_current_time(self, trip_duration):
        if self.remaining_trucks == 0:
            self.current_time += trip_duration

    def update_delivery_time(self, shipments):
        trip_duration = 0
        for package in shipments:
            duration = package.distance_in_km / self.max_speed
            package.estimated_delivery_time = round(duration + self.current_time, 2)
            trip_duration = max(trip_duration, duration)
        return trip_duration

    def generate_schedules(self):
        schedules = []
        while self.remaining_packages:
            if self.remaining_trucks == 0:
                self.remaining_trucks = self.available_trucks
                self.current_time += max(self.trip_duration)

            shipments = self.get_shipment(self.remaining_packages, self.remaining_trucks)
            trip_duration = self.update_delivery_time(shipments)
            self.remaining_trucks -= 1
            self.remaining_packages = [pkg for pkg in self.remaining_packages if pkg not in shipments]
            schedules.append(shipments)
            self.update_current_time(trip_duration)
        return schedules
