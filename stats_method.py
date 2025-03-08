
class Employee:
    def __init__(self, name, position):
        self.name = name 
        self.position = position

    def get_infor(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_positon(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position
    
employee1 = Employee("Eugune"," Manager")
employee2 = Employee("Squidar", "Cashier")
employee3 = Employee("Spongbob", "Cook")

print(Employee.is_valid_positon("Manager"))
print(employee1.get_infor())
print(employee2.get_infor())
print(employee3.get_infor())
