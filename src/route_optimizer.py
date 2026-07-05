import datetime

TRUCK_SPEED_MPH = 18
HUB_ADDRESS = "4001 South 700 East"


class RouteOptimizer:

    @staticmethod
    def deliver_packages(truck, hash_map, distance_matrix, address_lookup, package_9):
        print("Truck", truck.truck_number, "left the hub at", truck.time)

        for _ in truck.packages:
            optimal_distance = float("inf")
            optimal_package = None

            for package_id in truck.packages:
                if truck.time > datetime.timedelta(hours=10, minutes=20):
                    package_9.street = "410 S State St"

                current_package = hash_map.lookup(package_id)

                distance = distance_matrix[
                    address_lookup[truck.street]
                ][
                    address_lookup[current_package.street]
                ]

                if current_package.time_delivered is None and distance < optimal_distance:
                    optimal_package = current_package
                    optimal_distance = distance

            if optimal_package is not None:
                distance = distance_matrix[
                    address_lookup[truck.street]
                ][
                    address_lookup[optimal_package.street]
                ]

                truck.mileage += distance
                truck.time += datetime.timedelta(minutes=(distance / (TRUCK_SPEED_MPH * (1 / 60))))

                truck.street = optimal_package.street
                optimal_package.time_delivered = truck.time
                optimal_package.delivery_status = True
                optimal_package.truck_number = truck.truck_number

        distance = distance_matrix[address_lookup[truck.street]][address_lookup[HUB_ADDRESS]]
        truck.mileage += distance
        truck.time += datetime.timedelta(minutes=(distance / (TRUCK_SPEED_MPH * (1 / 60))))

        print("Truck", truck.truck_number, "returned to the hub at", truck.time)
        print()