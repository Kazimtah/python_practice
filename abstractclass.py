from abc import ABC, abstractmethod
class Vechile(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stope(self):
        pass


class Car(Vechile):
    def go(self):
        print("You drive the car")
    def stope(self):
        print('You stop the car')

class Motorcycle(Vechile):
    def go(self):
        print("You drive the Motorcycle")
    def stope(self):
        print("You stope the motorcycle")

class Boat(Vechile):
    def go(self):
        print("You sail the boat")
    def stope(self):
        print("You stop the boat")


boat1 = Boat()
boat1.go()
boat1.stope()


#car = Car()
#car.go()
#car.stope()
#motocyle = Motorcycle()
#motocyle.go()
#motocyle.stope()#