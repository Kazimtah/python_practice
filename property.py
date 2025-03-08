
class Rectangle:

    def __init__(self, widht, height):
        self._widht = widht
        self._height = height

    def __str__(self):
        return f"{self._widht} {self._height}"
    
    @property
    def width(self):
        return f"{self.width} = float({self._height})"

    @property
    def height(self):
        return f"{self.height} = float({self._height})"
    
    @width.setter
    def width(self, new_height):
        if new_height > 0:
            self._widht = new_height
        else:
            print("Widht must be greater than zero")

    @height.settter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")
    
    @width.deleter
    def width(self):
        del self._widht
        print("widht has been deleted!")
    
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

        
rectangle = Rectangle(3,4)
print(rectangle.width())
print(rectangle.height())