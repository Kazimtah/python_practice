class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

        
    def bark(self):
        print("Whoof Whoof")

class Owner:
    def __init__(self, owner_name, address, contac_number):
        self.owner_name = owner_name
        self.address = address
        self.contact_number = contac_number

owner1 = Owner("Danny", "122 Springfield Driver", "888-999")
dog1 = Dog("Bruce", "Scottisch Terrier",owner1)

#dog1.bark()
#print(dog1.name, dog1.breed)
print(dog1.owner.owner_name)
print(dog1.owner.address)
print()
print("*********************")


owner2 = Owner("Jhone", "Basel 2239 ", "618994778")
dog2 = Dog("Freya", "German Sheperd",owner2)
#dog2.bark()
#print(dog2.name, dog2.breed)
print(dog2.owner.owner_name)
print(dog2.owner.address)