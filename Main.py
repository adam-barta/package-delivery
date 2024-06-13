import csv

from HashTable import HashTable
from Package import Package


def load_package_data(filename, package_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            p_id = package[0]
            p_address = package[1]
            p_city = package[2]
            p_state = package[3]
            p_zipcode = package[4]
            p_deadline_time = package[5]
            p_weight = package[6]
            p_status = "At Hub"

            p = Package(p_id, p_address, p_city, p_state, p_zipcode, p_deadline_time, p_weight, p_status)

            # Insert data into hash table
            package_table.insert(p_id, p)


# Hash table instance
package_hash_table = HashTable()

# Load packages to Hash Table
load_package_data('PackageFile.csv', package_hash_table)

print(package_hash_table)