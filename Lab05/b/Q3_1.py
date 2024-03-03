class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bussy = Bus("School Volvo", 180, 12)
carry = Car("Audi Q5", 240, 18)
print(f"{bussy.color} {bussy.name} Speed: {bussy.max_speed} Mileage: {bussy.mileage}")
print(f"{carry.color} {carry.name} Speed: {carry.max_speed} Mileage: {carry.mileage}")