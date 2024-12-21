class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    def age(self, current_year):
        return current_year - self.birth_year
class Driver(Person):
    def __init__(self, name, birth_year, license_number):
        super().__init__(name, birth_year)
        self.license_number = license_number
    def __str__(self):
        return f"Driver: {self.name}, License: {self.license_number}"

person = Person("Таня", 1995)
print(f"{person.name} має {person.age(2024)} років.")

driver = Driver("Нік", 1990, "AB1234567")
print(driver)
print(f"{driver.name} має {driver.age(2024)} років.")
