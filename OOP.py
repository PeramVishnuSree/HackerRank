class vehicle:

    def __init__(self,name,max_speed,mileage,capacity):

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity*100

class Bus(vehicle):

    def fare(self):
        amount = super().fare()
        amount += amount*10/100
        return amount

School_Bus = Bus("Volvo", 180, 12, 100)
print(School_Bus.fare())
