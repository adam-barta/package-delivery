import datetime


class Package:
    def __init__(self, pid, address, city, state, zipcode, deadline_time, weight, status):
        self.pid = pid
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline_time = deadline_time
        self.weight = weight
        self.status = status
        self.time_left_hub = None
        self.delivery_time = None

    def __str__(self):
        # Build the string with package details
        package_string = f"Package ID: {self.pid}\n"
        package_string += f"  Address: {self.address}\n"
        package_string += f"  City: {self.city}\n"
        package_string += f"  State: {self.state}\n"
        package_string += f"  Zipcode: {self.zipcode}\n"
        package_string += f"  Weight: {self.weight}\n"
        package_string += f"  Status: {self.status}\n"
        package_string += f"  Time left hub: {self.time_left_hub}\n"
        package_string += f"  Delivery time: {self.delivery_time}\n"
        package_string += f"  Deadline: {self.deadline_time}\n"
        package_string += "---\n"
        return package_string

    def check_status(self, current_time):
        if self.time_left_hub > current_time:
            self.status = "At Hub"
            self.delivery_time = None
            self.time_left_hub = None
        elif self.delivery_time > current_time:
            self.status = "En route"
            self.delivery_time = None
        else:
            self.status = "Delivered"
        if self.pid == 9:
            if current_time > datetime.timedelta(seconds=37200):
                self.address = "410 S. State St"
                self.city = "Salt Lake City"
                self.state = "UT"
                self.zipcode = "84111"
