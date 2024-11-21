"""
Завдання 3: Принцип підстановки Лісков (Liskov Substitution Principle - LSP)

Створіть ієрархію класів для геометричних фігур, де кожен підклас (наприклад, "Квадрат" і "Круг")
може замінити базовий клас "Фігура" без порушення функціональності. Переконайтеся,
що ці підкласи можуть використовуватися замість базового класу у всіх контекстах без проблем.
"""
class Shape():
    def __init__(self, name):
        self.name = name

    def get_shape_info(self):
        print(f"Thi figure is {self.name}")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def get_shape_info(self):
        print(f"This is {self.name} with radius {self.radius}")

class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def get_shape_info(self):
        print(f"This is {self.name} with side {self.side}")

figure1 = Circle(5)
figure2 = Square(12)
figure1.get_shape_info()
figure2.get_shape_info()
figure3 = Shape("figa")
figure3.get_shape_info()