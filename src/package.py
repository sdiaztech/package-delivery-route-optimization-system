class Package:
    def __init__(self, id, street, city, state, zip, deadline, weight, special_notes):
        self.id = id
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.time_delivered = None
        self.delivery_status = False
        self.truck_number = 0

    def __str__(self):
        return "%s, %s, %s, %s, %s ,%s, %s, %s" % (
            self.id, self.street, self.city, self.state, self.zip, self.deadline, self.weight,
            self.special_notes)
