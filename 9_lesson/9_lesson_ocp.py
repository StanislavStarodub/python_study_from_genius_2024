"""
Завдання 2: Принцип відкритості/закритості (Open/Closed Principle - OCP)

Створіть інтерфейс "Фігура" (Shape) та два класи, які реалізують цей інтерфейс, наприклад,
"Коло" (Circle) та "Прямокутник" (Rectangle).
Потім додайте новий клас, який розраховує площу будь-якої фігури, не модифікуючи існуючі класи.
Використовуйте принцип OCP для розширення функціональності.
"""
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def get_area():
        pass

    @abstractmethod
    def __str__(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 2 * pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius}"

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return 0.5 * self.width * self.height

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}"

class CalcArea():

    @staticmethod
    def calc_area(shape: Shape):
        print(f"The area of {shape} is {shape.get_area()}")

circle = Circle(4)
rectangle = Rectangle(3, 6)

CalcArea.calc_area(circle)
CalcArea.calc_area(rectangle)