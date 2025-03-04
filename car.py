from main import Car

car1 = Car("Mustang", 2024, "red", False)
print(car1.model, car1.year,car1.color, car1.for_sale)
car2 = Car("Covertte", 2025, "blue", True)
print(car2.model, car2.color, car2.for_sale,car2.year)
car3 = Car("Charger", 2026, "yellow", True)
print(car3.model, car3.year, car3.color, car3.for_sale)

car1.stop()
car1.describe()