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
    return distance_csv[address1_index][address2_index]


# Algorithm to deliver packages and update package and truck status
def deliver_packages(truck):
    truck.current_location = "4001 South 700 East"
    truck.mileage = 0.0
    truck.current_time = datetime.timedelta(hours=8, minutes=0)
    truck_speed = 18  # miles per hour as given

    while len(truck.packages) > 0:
        min_distance = 2000  # miles
        closest_package = None  # no package

        for packageID in truck.packages:
            package = package_hash_table.search(packageID)
            truck_location = truck.current_location
            package_address = package.address
            distance = distance_between(truck_location, package_address)

            if distance < min_distance:
                min_distance = distance
                closest_package = package

        truck.mileage += min_distance
        truck.current_time += (min_distance / truck_speed)
        closest_package.delivery_time = truck.current_time
        closest_package.delivery_status = "Delivered"
        truck.current_location = closest_package.address
        truck.packages.remove(closest_package.ID)


# Create hash table instance
package_hash_table = HashTable()

# Load packages into hash table
load_package_data(package_csv, package_hash_table)

# Create truck instance truck1
# Create truck instance truck1
truck1 = Truck([2, 4, 5], 0.0, "4001 South 700 East", datetime.timedelta(hours=8))
deliver_packages(truck1)
