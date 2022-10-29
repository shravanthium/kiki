import argparse
from courier import Courier


parser = argparse.ArgumentParser(description="Delivery Estimation")
parser.add_argument("base_delivery_cost", type=int, help="Base delivery cost")
parser.add_argument("no_of_packges", type=int, help="Total number of packages")
parser.add_argument(
    "-pkgs",
    nargs="+",
    required=True,
    help="One or more package details: base_delivery_cost,pkg_weight_in_kg,distance_in_km",
)
args = parser.parse_args()


if __name__ == "__main__":
    base_delivery_cost = args.base_delivery_cost
    no_of_packges = args.no_of_packges
    packages = args.pkgs

    for package in packages:
        id, weight, distance, offer = package.split(",")
        current_package = Courier(base_delivery_cost, int(weight), int(distance), offer)
        discount = current_package.discount()
        total_cost = current_package.total_cost()
        print(id, discount, total_cost)
