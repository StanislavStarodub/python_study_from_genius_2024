"""
**Завдання 1: Створення класу і об'єктів**

Створіть клас `Animal`, який представляє тварину. Кожний об'єкт класу `Animal`
повинен мати наступні атрибути:

- `name` (ім'я тварини)
- `species` (вид тварини)
- `age` (вік тварини)

Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта.
Напишіть метод `make_sound()`, який буде виводити звук, який виділяє тварина.

Створіть два об'єкта класу `Animal` з різними характеристиками та
викличте їхні методи `make_sound()`.
"""

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self, sound):
        self.sound = sound
        return f"The {self.species} named {self.name} makes a sound {self.sound}!"

animal1 = Animal("Bobik", "dog", 2)
animal2 = Animal("Murka", "cat", 9)
print(animal1.make_sound("Gafff, Gafff, Gafff"))
print(animal2.make_sound("Myauuu, Myauuu, Myauuu"))

"""
**Завдання 2: Робота з об'єктами**

Створіть клас `Rectangle`, який представляє прямокутник. Кожен об'єкт класу `Rectangle`
повинен мати наступні атрибути:

- `width` (ширина прямокутника)
- `height` (висота прямокутника)

Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта.
Напишіть метод `calculate_area()`, який розраховує площу прямокутника (площа = ширина * висота).

Створіть два об'єкта класу `Rectangle` з різними розмірами та викличте їхні
методи `calculate_area()`, виведіть площу прямокутників на екран.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return f"The area of the rectangle id {self.width * self.height}"

first_rectangle = Rectangle(7, 9)
second_rectangle = Rectangle(205, 3)
print(first_rectangle.calculate_area())
print(second_rectangle.calculate_area())
