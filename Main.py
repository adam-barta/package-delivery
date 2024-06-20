import csv
import datetime

from HashTable import HashTable
from Package import Package
from Truck import Truck

# Open and read addressCSV file
with open("address.csv") as csvfile:
    address_csv = list(csv.reader(csvfile))

# Open and read distanceCSV file
with open("distance.csv") as csvfile:
    distance_csv = list(csv.reader(csvfile))

# Open and read packageCSV file
with open("package.csv") as csvfile:
    package_csv = list(csv.reader(csvfile))


# Load package data into hash table
def load_package_data(package_data, package_table):
    for package in package_data:
        pid = int(package[0])
        address = package[1]
        city = package[2]
        state = package[3]
        zipcode = package[4]
        deadline_time = package[5]
        weight = package[6]
        status = "At hub"

        p = Package(pid, address, city, state, zipcode, deadline_time, weight, status)

        # Insert data into hash table
        package_table.insert(pid, p)


# Extract address from address_csv
def extract_address(address):
    for row in address_csv:
        if address in row[2]:
            return int(row[0])


# Find distance between two addresses
# def distance_between(address1, address2):
#     return float(distance_csv[address1][address2])
def distance_between(address1, address2):
    address1_index = extract_address(address1)
    address2_index = extract_address(address2)
    distance = distance_csv[address1_index][address2_index]
    if distance == '':
        distance = distance_csv[address2_index][address1_index]
    return float(distance)


# Algorithm to deliver packages and update package and truck status
def deliver_packages(truck):
    truck_speed = 18  # miles per hour

    # Update time_left_hub for all packages on truck
    for packageID in truck.packages:
        package = package_hash_table.search(packageID)
        package.time_left_hub = truck.current_time

    while len(truck.packages) > 0:
        min_distance = 2000  # miles
        closest_package = None

        for packageID in truck.packages:
            package = package_hash_table.search(packageID)
            truck_location = truck.current_location
            package_address = package.address
            distance = distance_between(truck_location, package_address)

            if distance < min_distance:
                min_distance = distance
                closest_package = package

        truck.mileage += min_distance
        truck.current_time += datetime.timedelta(hours=min_distance / truck_speed)
        closest_package.delivery_time = truck.current_time
        closest_package.status = "Delivered"
        truck.current_location = closest_package.address
        truck.packages.remove(closest_package.pid)

    # Add distance and time to hub to truck object after all packages are delivered.
    distance_to_hub = distance_between(truck.current_location, "4001 South 700 East")
    truck.mileage += distance_to_hub
    truck.current_time += datetime.timedelta(hours=distance_to_hub / truck_speed)


# Create hash table instance
package_hash_table = HashTable()

# Load packages into hash table
load_package_data(package_csv, package_hash_table)

# Create truck instance truck1
# Create truck instance truck1
truck1 = Truck([1, 2, 4, 5, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 0.0,
               "4001 South 700 East", datetime.timedelta(hours=8, minutes=0))
truck2 = Truck([3, 6, 7, 8, 10, 11, 12, 17, 18, 21, 22, 28, 32, 36, 38], 0.0,
               "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))
truck3 = Truck([9, 23, 24, 25, 26, 27, 33, 35, 39], 0.0,
               "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

deliver_packages(truck1)
deliver_packages(truck2)
deliver_packages(truck3)

# Iterate through all buckets and print package details
for bucket in package_hash_table.table:
    for key, package in bucket:
        print(f"Package ID: {key}")
        # print(f"  Address: {package.address}")
        # print(f"  City: {package.city}")
        # print(f"  State: {package.state}")
        # print(f"  Zipcode: {package.zipcode}")
        # print(f"  Weight: {package.weight}")
        # print(f"  Status: {package.status}")
        print(f"  Delivery time: {package.delivery_time}")
        print(f"  Deadline: {package.deadline_time}")
        # print(f"  Time left hub: {package.time_left_hub}")
        print("---")  # Separator between packages

print(str(truck1))
print(str(truck2))
print(str(truck3))

print(f"Mileage is {truck1.mileage + truck2.mileage + truck3.mileage}")

# TODO - Write code for UI
