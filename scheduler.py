class Scheduler:
    def __init__(self, packages, max_load_capacity, available_trucks, max_speed):
        self.packages = packages
        self.max_load_capacity = max_load_capacity
        self.available_trucks = available_trucks
        self.current_time = 0
        self.remaining_packages = packages
        self.remaining_trucks = available_trucks
        self.max_speed = max_speed
        self.trip_duration = []

    def get_shipment(self):
        possible_shipments = {}
        trip_weight = 0
        if not self.remaining_packages:
            return []

        for i in range(0, len(self.remaining_packages)):
            current_max_weight = self.remaining_packages[i].pkg_weight_in_kg
            max_weight = self.remaining_packages[i].pkg_weight_in_kg
            shipments = []

            for j in range(1, len(self.remaining_packages)):
                current_max_weight += self.remaining_packages[j].pkg_weight_in_kg

                if current_max_weight < self.max_load_capacity:
                    shipments.append(self.remaining_packages[j])
                    max_weight += self.remaining_packages[j].pkg_weight_in_kg
                current_max_weight -= self.remaining_packages[j].pkg_weight_in_kg

            if max_weight == 0:
                max_weight = self.remaining_packages[i].pkg_weight_in_kg

            if not shipments:
                shipments.append(self.remaining_packages[i])

            possible_shipments[max_weight] = shipments
            trip_weight = max(trip_weight, max_weight)

        self.remaining_trucks -= 1
        self.update_remaining_packages(possible_shipments[trip_weight])
        return possible_shipments[trip_weight]

    def update_remaining_packages(self, shipments):
        current_remaining_packages = [
            package for package in self.remaining_packages if package not in shipments
        ]
        self.remaining_packages = current_remaining_packages
        return self.remaining_packages

    def update_current_time(self):
        if self.remaining_trucks == 0:
            self.current_time += min(self.trip_duration)
        return self.current_time

    def update_delivery_time(self, shipments):
        trip_duration = 0

        if not shipments:
            return trip_duration

        for package in shipments:
            duration = (
                round((package.distance_in_km / self.max_speed), 2) + self.current_time
            )
            package.estimated_delivery_time = duration
            trip_duration = max(duration, trip_duration)
        trip_duration *= 2
        self.trip_duration.append(trip_duration)
        self.update_current_time()
        return trip_duration

    def generate_schedules(self):

        while len(self.remaining_packages) > 0:
            if self.remaining_trucks == 0:
                self.remaining_trucks = self.available_trucks
                self.trip_duration = []

            shipments = self.get_shipment()
            self.update_delivery_time(shipments)
