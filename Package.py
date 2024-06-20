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
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.pid, self.address, self.city, self.state, self.zipcode,
                                                       self.deadline_time, self.weight, self.time_left_hub,
                                                       self.delivery_time)
