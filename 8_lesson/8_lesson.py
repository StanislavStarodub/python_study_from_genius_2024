"""
Завдання 1: Інкапсуляція

Створіть клас "Користувач" (User), який має такі приватні поля (інкапсульовані дані):

Ім'я (name)
Електронна пошта (email)
Пароль (password)
Напишіть публічні методи для установки і отримання значень цих полів (геттери і сеттери).
Потім створіть об'єкт класу "Користувач" і встановіть значення полів, а також виведіть їх на екран.
"""
class User:
    def __init__(self, name, email, password):
        # Всі змінні приватні
        self.__name = name
        self.__email = email
        self.__password = password

    def get_user_all_info(self):
        print("<_____________>")
        # Увага, буде виводитись приватне ім'я
        print(f"All info for user {self.__name} are {self.__dict__}")
        print("<_____________>")

    def get_user_name(self):
        # Увага, буде виводитись приватне ім'я
        print(f"The username is {self.__name}")

    def __check_attribute_type(self, attr, should_be):
        if type(attr) == should_be:
            return True
        else:
            raise TypeError(f"Attribute must be {should_be}")

    def set_user_attr(self, attr, value):
         if self.__check_attribute_type(attr, str):
             self.__dict__[attr] = value
             return {attr : self.__dict__[attr]}
         else:
             print("Attribute must be string type")


user_ivanov = User("a", "b", "c")
user_ivanov.get_user_all_info()

ivanov_attrs = {'name' : "Serg", 'email' : "ari@gmail.com", 'password' : "crazy_Monkey7"}
for key, value in ivanov_attrs.items():
    user_ivanov.set_user_attr(key, value)

# Всі приватні дані залишились, як були створені
user_ivanov.get_user_all_info()
user_ivanov.get_user_name()
print(user_ivanov.__dict__['name'])

"""
Завдання 2: Абстракція

Створіть клас "Фігура" (Shape), який буде абстрактним класом. У цьому класі визначіть абстрактний метод
 "обчислити_площу" (calculate_area).

Створіть підкласи цього класу для різних геометричних фігур, наприклад, "Коло" (Circle), 
"Прямокутник" (Rectangle) і "Трикутник" (Triangle). У кожному з підкласів реалізуйте метод 
"обчислити_площу" відповідно до формули для обчислення площі кожної фігури.

Створіть об'єкти кожного з підкласів і використайте метод "обчислити_площу", 
щоб вивести площу кожної фігури на екран.
"""

from abc import ABC, abstractclassmethod

class Shape(ABC):

    @abstractclassmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print(f"The circle area is {3.14 * self.radius ** 2}")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        print(f"The rectangle area is {0.5 * self.width * self.height}")

class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def calculate_area(self):
        print(f"The triangle area is {0.5 * self.base * self.height}")

circle = Circle(7.7)
rectangle = Rectangle(3, 8)
triangle = Triangle(8, 16)
circle.calculate_area()
rectangle.calculate_area()
triangle.calculate_area()