import argparse
from courier import Courier
from scheduler import Scheduler
from utils import __display__

parser = argparse.ArgumentParser(description="Delivery Estimation")
parser.add_argument("base_delivery_cost", type=int, help="Base delivery cost")
parser.add_argument("no_of_packges", type=int, help="Total number of packages")
parser.add_argument(
    "-pkgs",
    nargs="+",
    required=True,
    help="Package details: base_delivery_cost,pkg_weight_in_kg,distance_in_km",
)
parser.add_argument(
    "-v",
    nargs="+",
    help="Vehicle details:  max_load_capacity, available_trucks, max_speed",
)
args = parser.parse_args()


if __name__ == "__main__":
    packages = []
    show_eta = False
    packages_details = args.pkgs
    no_of_packges = args.no_of_packges
    base_delivery_cost = args.base_delivery_cost
    available_trucks, max_speed, max_load_capacity = 0, 0, 0

    for package in packages_details:
        id, weight, distance, offer = package.split(",")
        current_package = Courier(
            id, base_delivery_cost, int(weight), int(distance), offer
        )
        packages.append(current_package)
        discount = current_package.discount()
        total_cost = current_package.total_cost()

    if args.v:
        vehicle_details = args.v[0].split(",")
        show_eta = True
        available_trucks, max_speed, max_load_capacity = (
            int(vehicle_details[0]),
            int(vehicle_details[1]),
            int(vehicle_details[2]),
        )
        scheduler_service = Scheduler(
            packages, max_load_capacity, available_trucks, max_speed
        )
        shipments = scheduler_service.generate_schedules()

    __display__(packages, show_eta=show_eta)
