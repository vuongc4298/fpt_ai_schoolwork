class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
bugatti = Vehicle(240, 18)
print(f"{bugatti.max_speed} {bugatti.mileage}")