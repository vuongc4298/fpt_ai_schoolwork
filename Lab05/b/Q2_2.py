class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capcity of a {self.name} is {capacity} passengers"
    
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity)

bussy = Bus("School Volvo", 180, 12)
print(bussy.seating_capacity())