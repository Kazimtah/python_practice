from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (3.14 * pow(self.radius,2))


class Square(Shape):
    def __init__(self, width):
        self.width = width
    
    def area(self):
        return (self.width * self.width)

    


class Traiangle(Shape):
    def __init__(self, base, heigth):
        self.base = base
        self.height = heigth

    def area(self):
        return ((self.base * self.height)/2)
    

shapes = [Circle(5), Square(3), Traiangle(4,6)]

for shape in shapes:
    print(shape.area())
