# Create class for freight trucks
class Truck:
    # Truck object constructor
    def __init__(self, name, packages, mileage, current_location, current_time):
        self.truck_name = name
        self.packages = packages
        self.mileage = mileage
        self.current_location = current_location
        self.current_time = current_time
