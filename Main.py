# Adam Barta - ID #011226755
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

        # Create package objects
        p = Package(pid, address, city, state, zipcode, deadline_time, weight, status)

        # Insert package objects into hash table
        package_table.insert(pid, p)


# Extract address from address_csv
def extract_address(address):
    for row in address_csv:
        if address in row[2]:
            return int(row[0])


# Find distance between two addresses

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
        package.truck = truck.truck_name

    # Loop until truck is empty
    while len(truck.packages) > 0:
        min_distance = 2000  # miles
        closest_package = None

        # Loop through all package on truck and find min_distance (i.e. nearest neighbor)
        for packageID in truck.packages:
            package = package_hash_table.search(packageID)
            truck_location = truck.current_location
            package_address = package.address
            distance = distance_between(truck_location, package_address)

            if distance < min_distance:
                min_distance = distance
                closest_package = package

        # Update truck mileage, time and status. Update package status and remove from truck
        truck.mileage += min_distance
        truck.current_time += datetime.timedelta(hours=min_distance / truck_speed)
        closest_package.delivery_time = truck.current_time
        closest_package.status = "Delivered"
        truck.current_location = closest_package.address
        truck.packages.remove(closest_package.pid)

    # Add distance and time to hub to truck after all packages are delivered.
    distance_to_hub = distance_between(truck.current_location, "4001 South 700 East")
    truck.mileage += distance_to_hub
    truck.current_time += datetime.timedelta(hours=distance_to_hub / truck_speed)


# Create hash table instance
package_hash_table = HashTable()

# Load packages into hash table
load_package_data(package_csv, package_hash_table)

# Create truck instances
truck1 = Truck("Truck 1", [1, 2, 4, 5, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 0.0,
               "4001 South 700 East", datetime.timedelta(hours=8, minutes=0))
truck2 = Truck("Truck 2", [3, 6, 17, 18, 21, 22, 25, 28, 32, 36, 38], 0.0,
               "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))
truck3 = Truck("Truck 3", [7, 8, 9, 10, 11, 12, 23, 24, 26, 27, 33, 35, 39], 0.0,
               "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# Correct package #9 address
package9 = package_hash_table.search(9)
package9.address = "410 S State St"
package9.city = "Salt Lake City"
package9.state = "UT"
package9.zipcode = "84111"

# Call delivery algorithm
deliver_packages(truck1)
deliver_packages(truck2)
deliver_packages(truck3)


class Main:
    # Code for UI
    # Source: ASCII art from https://ascii-generator.site/
    title = ''' __      __    ________   ____ ___  __________    _________ 
/  \    /  \  /  _____/  |    |   \ \______   \  /   _____/ 
\   \/\/   / /   \  ___  |    |   /  |     ___/  \_____  \  
 \        /  \    \_\  \ |    |  /   |    |      /        \ 
  \__/\  /    \______  / |______/    |____|     /_______  / 
       \/            \/                                 \/'''
    print(title)
    print("Welcome to the Western Governors University Parcel Service")
    print(f"Mileage for truck 1 is {truck1.mileage} mi.")
    print(f"Mileage for truck 2 is {truck2.mileage} mi.")
    print(f"Mileage for truck 3 is {truck3.mileage} mi.")
    print(f"Total mileage for current route is {truck1.mileage + truck2.mileage + truck3.mileage} mi.")

    # Loop until valid time or exit from program is input
    while True:
        try:
            user_time = input("Enter a time to check status (Format: HH:MM:SS) or 'exit' to exit: ")
            if user_time == "exit":
                exit()
            (h, m, s) = user_time.split(":")
            user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            break
        except ValueError:
            print("Invalid time format, please try again.")

    # Display all or single package status
    text = input("To view status of a single package type '1'. For status of all packages type '2': ")
    if text == "1":
        try:
            solo_input = input("Enter package ID: ")
            package = package_hash_table.search(int(solo_input))
            package.check_status(user_time)
            print(str(package))
        except ValueError:
            print("Invalid entry")
            exit()
    elif text == "2":
        try:
            for packageID in range(1, 41):
                package = package_hash_table.search(packageID)
                package.check_status(user_time)
                print(str(package))
        except ValueError:
            print("Invalid entry")
            exit()
    else:
        exit()
