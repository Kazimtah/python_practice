class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_detaisl(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name 
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position) 
        self.employees.append(new_employee)

    def list_employee(self):
        return list(employee.get_detaisl()for employee in self.employees)

company = Company("Krusty Krab")
company.add_employee("Eugee", "Manager")
company.add_employee("Squidward", "Cashier")
print(company.company_name)

company1 = Company("Chum Buck")
company1.add_employee("Sheldon", "Manager")
company1.add_employee("Karen", "Assisten")
print(company.company_name)

print(company.list_employee())

for employee in company1.list_employee():
    print(employee)