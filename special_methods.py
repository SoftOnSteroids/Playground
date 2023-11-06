class Car:
    def __init__(self, wheels = 4, doors = 5, speed = 150):
        self.wheels= wheels
        self.doors= doors
        self.speed= speed
    
    def __mul__(self, other):
        return Car(self.wheels * other.wheels, self.doors * other.doors, self.speed * other.speed)

    def __add__(self, other):
        # return Car(self.wheels + other.wheels, self.doors + other.doors, self.speed + other.speed)
        return [self, other]
    
    def __repr__(self):
        return f"Car({self.wheels}, {self.doors}, {self.speed})"
        
if __name__ == "__main__":
    car1 = Car()
    car2 = Car()

    print(f"car1: {car1}, car2: {car2}")
    print(f"car1 + car2: {car1 + car2}")
    print(f"car1 * car2: {car1 * car2}")