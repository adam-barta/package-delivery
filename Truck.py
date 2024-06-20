# Create class for freight trucks
class Truck:
    def __init__(self, packages, mileage, current_location, current_time):
        self.packages = packages
        self.mileage = mileage
        self.current_location = current_location
        self.current_time = current_time

    def __str__(self):
        return "%s, %s, %s, %s" % (self.packages, self.mileage, self.current_location, self.current_time)
