class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power


class Wheel:
    def __init__(self, wheel_size):
        self.wheel_size = wheel_size


class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engin = Engine(horse_power)
        self.wheel = [Wheel(wheel_size) for wheel in range(4)]
    def display_car(self):
        return f"{self.make} {self.model} {self.engin.horse_power} {self.wheel[0].wheel_size}"


car = Car("Ford", "Mustang", 500, 18)
print(car.display_car())