class Truck:
    def __init__(self, packages, street, mileage, time, truck_number):
        self.packages = packages
        self.street = street
        self.mileage = mileage
        self.time = time
        self.truck_number = truck_number

    def __str__(self):
        return (
            f"{self.packages}, {self.street}, "
            f"{self.mileage}, {self.time}"
        )