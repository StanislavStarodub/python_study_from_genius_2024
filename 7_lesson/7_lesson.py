"""
**Завдання 1: Наслідування**

Створіть базовий клас `Vehicle` (транспортний засіб), який містить наступні атрибути:

- `make` (виробник)
- `model` (модель)
- `year` (рік виробництва)

Додайте конструктор класу `Vehicle`, який ініціалізує ці атрибути.

Створіть підкласи (похідні класи) від `Vehicle` для різних видів транспорту, наприклад,
`Car`, `Motorcycle`, `Bicycle`, тощо. Кожен підклас повинен мати додаткові атрибути та методи,
 які є специфічними для цього виду транспорту. Наприклад, для класу `Car` можна додати атрибут `fuel_type`
  та метод `start_engine()`.

Створіть об'єкти для кожного з підкласів та виведіть їхні атрибути на екран.
"""

"""
**Завдання 2: Поліморфізм**

Створіть метод `display_info()` у базовому класі `Vehicle`, який виводить загальну інформацію про 
транспортний засіб (наприклад, "Це [виробник] [модель] [рік] року виробництва.").

В кожному з підкласів перевизначте метод `display_info()` для виведення специфічної інформації про
 цей вид транспорту.

Створіть список об'єктів з різних видів транспорту, викличте метод `display_info()` для кожного об'єкта,
і спостерігайте за тим, як поліморфізм дозволяє викликати правильну версію методу для кожного об'єкта.
"""
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info():
        print(f"This is {self.make} {self.model} {self.year} of manufacture")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"The car {self.make} {self.model} starts with {self.fuel_type} engine")

    def display_info(self):
        print(f"This is {self.make} {self.model} {self.year} of manufacture has a {self.fuel_type} engine")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, weels):
        super().__init__(make, model, year)
        self.weels = weels

    def speed(self):
        print(f"The speed of motorcycle {self.make} {self.model} with {self.weels} weels is more than a car one")

    def display_info(self):
        print(f"This is {self.make} {self.model} {self.year} of manufacture has {self.weels} weels")

car_volvo = Car("Volvo", "GX300", 2017, "gas")
car_volvo.start_engine()
print(car_volvo.__dict__)
moto_honda = Motorcycle("Honda", "CH900", 2021, 2)
moto_honda.speed()
print(moto_honda.__dict__)
print("____________________")
car_ford = Car("Ford", "Focus", 2023, "electric")
for vehicle in (car_volvo, moto_honda, car_ford):
    vehicle.display_info()
    print("<____________________>")