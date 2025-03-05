class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Cirlcle(Shape):
    
    def __init__(self, color, is_filled,  radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def describe(self):
        super().describe()
        print(f"It is the circle with an area of {3.14*(self.radius*self.radius)}")
    
        
class Squar(Shape):
    def __init__(self,color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        print(f"It is the square with the area of {self.width*self.width}cm^2")


class Triangle(Shape):
    def __init__(self, color, is_filled,  width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height 
    def describe(self):
        print(f"The total area of triangle is {0.5*self.width*self.height}")

circle = Cirlcle("red", True, 5)
print(circle.describe())
#print(circle.color)
#print(circle.radius)
#print(circle.is_filled)

square = Squar(color= "blue", is_filled= True, width= 5)
print(square.describe())

#print(square.color)
#print(square.is_filled)
#print(square.width)

traiangle = Triangle("yellow", True, width=5, height=4)
print(traiangle.describe())