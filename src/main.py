"""
Author:         Samuel Diaz #001361588
Title:          WGUPS Routing Project
Description:    Program determines an efficient route and delivery distribution option for packages distributed by WGUPS, a parcel distributor.
Course:         C950 - Data Structures and Algorithms II
Sources:        Zybooks textbook - Data Structures and Algorithms II
"""

import csv
import datetime
from hashmap import HashMap
from truck import Truck
from package import Package
from route_optimizer import RouteOptimizer


PACKAGES_CSV_PATH = 'data/packages.csv'
DISTANCE_MATRIX_CSV_PATH = 'data/distance_matrix.csv'
ADDRESSES_CSV_PATH = 'data/addresses.csv'
HUB_ADDRESS = "4001 South 700 East"


def load_packages(csv_path):
    packages = []

    with open(csv_path, "r", encoding="utf-8-sig") as package_file:
        csv_reader = csv.reader(package_file, delimiter=",")

        for row in csv_reader:
            package = Package(
                int(row[0]),
                row[1],
                row[2],
                row[3],
                int(row[4]),
                row[5],
                int(row[6]),
                row[7],
            )
            packages.append(package)

    return packages


def load_address_lookup(csv_path):
    address_lookup = {}

    with open(csv_path, "r", encoding="utf-8-sig") as address_file:
        for index, address in enumerate(address_file):
            address_lookup[address.strip()] = index

    return address_lookup


packages = load_packages(PACKAGES_CSV_PATH)
packages_by_id = {package.id: package for package in packages}
package_9 = packages_by_id[9]

hash_map = HashMap()

for package_object in packages:
    hash_map.insert(package_object.id, package_object)

with open(DISTANCE_MATRIX_CSV_PATH, 'r', encoding='utf-8-sig') as data:
    distance_matrix = []
    csv_reader = csv.reader(data, delimiter=',')

    for row in csv_reader:
        row_list = []

        for cell in row:
            cell = float(cell)
            row_list.append(cell)

        distance_matrix.append(row_list)

address_lookup = load_address_lookup(ADDRESSES_CSV_PATH)

truck_1_package_ids = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 39, 40]
truck_1_departure_time = datetime.timedelta(hours=8, minutes=0)
truck_1 = Truck(truck_1_package_ids, HUB_ADDRESS, 0, truck_1_departure_time, 1)

truck_2_package_ids = [3, 6, 18, 23, 24, 25, 26, 27, 28, 32, 33, 35, 36, 38]
truck_2_departure_time = datetime.timedelta(hours=9, minutes=5)
truck_2 = Truck(truck_2_package_ids, HUB_ADDRESS, 0, truck_2_departure_time, 2)

truck_3_package_ids = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 19, 21, 22]
truck_3_departure_time = datetime.timedelta(hours=10, minutes=0)
truck_3 = Truck(truck_3_package_ids, HUB_ADDRESS, 0, truck_3_departure_time, 3)

RouteOptimizer.deliver_packages(truck_1, hash_map, distance_matrix, address_lookup, package_9)
RouteOptimizer.deliver_packages(truck_2, hash_map, distance_matrix, address_lookup, package_9)
RouteOptimizer.deliver_packages(truck_3, hash_map, distance_matrix, address_lookup, package_9)


def all_packages_at_specified_time(hr, mins):
    specified_time = datetime.timedelta(hours=hr, minutes=mins)
    print("\nDelivery status for all packages at", specified_time)

    for p in packages:
        package = hash_map.lookup(p.id)
        delivery_stats = ""

        if package.truck_number == 1:
            if specified_time <= truck_1_departure_time:
                delivery_stats = "at the hub"
            elif truck_1_departure_time < specified_time < package.time_delivered:
                delivery_stats = "en route"
            elif specified_time >= package.time_delivered:
                delivery_stats = "delivered"
        if package.truck_number == 2:
            if specified_time <= truck_2_departure_time:
                delivery_stats = "at the hub"
            elif truck_2_departure_time < specified_time < package.time_delivered:
                delivery_stats = "en route"
            elif specified_time >= package.time_delivered:
                delivery_stats = "delivered"
        if package.truck_number == 3:
            if specified_time <= truck_3_departure_time:
                delivery_stats = "at the hub"
            elif truck_3_departure_time < specified_time < package.time_delivered:
                delivery_stats = "en route"
            elif specified_time >= package.time_delivered:
                delivery_stats = "delivered"

        print("Package", package.id, "|", delivery_stats)


print("---------------------------------------------------------------------------------------------")
all_packages_at_specified_time(9, 20)
print("---------------------------------------------------------------------------------------------")
all_packages_at_specified_time(10, 20)
print("---------------------------------------------------------------------------------------------")
all_packages_at_specified_time(13, 00)

while True:
    user_choice = int(input('\n-----------------------------------------------------------------------------------'
                            '\nRetrieve Package Status (1) | Display Total Mileage (2) | Quit (3)'
                            '\nMenu choice: '))

    if user_choice == 1:
        input_package_id = int(input('\n\nInput package ID (1-40): '))
        input_hours = int(input('\nHour(1-24): '))
        input_minutes = int(input('\nMinutes(1-60): '))

        input_time = datetime.timedelta(hours=input_hours, minutes=input_minutes)
        input_package = hash_map.lookup(input_package_id)
        status_message = ""

        if input_package.truck_number == 1:
            if input_time <= truck_1_departure_time:
                status_message = "at the hub"
            elif truck_1_departure_time < input_time < input_package.time_delivered:
                status_message = "en route"
            elif input_time >= input_package.time_delivered:
                status_message = "delivered"
        elif input_package.truck_number == 2:
            if input_time <= truck_2_departure_time:
                status_message = "at the hub"
            elif truck_2_departure_time < input_time < input_package.time_delivered:
                status_message = "en route"
            elif input_time >= input_package.time_delivered:
                status_message = "delivered"
        elif input_package.truck_number == 3:
            if input_time <= truck_3_departure_time:
                status_message = "at the hub"
            elif truck_3_departure_time < input_time < input_package.time_delivered:
                status_message = "en route"
            elif input_time >= input_package.time_delivered:
                status_message = "delivered"

        print(input_package)
        print("\n\nPackage ID:", input_package.id, "| Requested time:", input_time,
              "\n---------------------------------------------------------------"
              "\n  Status:", status_message,
              "\n  Time delivered", input_package.time_delivered,
              "\n  Deadline:", input_package.deadline,
              "\n  Address: ", input_package.street, input_package.city, input_package.state, input_package.zip,
              "\n  Weight:", input_package.weight, "lbs",
              "\n  Special notes:", input_package.special_notes,
              "\n  Truck number:", input_package.truck_number)

    if user_choice == 2:
        combined_miles = truck_1.mileage + truck_2.mileage + truck_3.mileage
        print("\n\nAll trucks combined drove a total of", round(combined_miles, 2), "miles.")

    if user_choice == 3:
        break