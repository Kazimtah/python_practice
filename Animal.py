class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = False
    def eat(self):
        print(f"{self.name} is eating")
    def sleeping(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOAF")
class Cat(Animal):
    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def speak(self):
        print("SQUO")

dog = Dog("Scoby")
dog.eat()
dog.speak()
cat = Cat("Garfield")
cat.eat()
cat.speak()
mouse = Mouse("Mickey")
mouse.eat()
mouse.speak()

#print(dog.name, dog.is_alive)