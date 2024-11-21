"""
Завдання 4: Принцип інтерфейсу користувача (Interface Segregation Principle - ISP)

Розробіть інтерфейс "Мережевий принтер" (NetworkPrinter), який включає методи для друку,
 сканування та копіювання. Потім створіть два класи: "Принтер" (Printer) та "Сканер" (Scanner),
  які реалізують цей інтерфейс та використовують лише ті методи, які їм потрібні. Переконайтеся,
  що жоден з класів не має пустого методу.
"""
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Scanable(ABC):
    @abstractmethod
    def scan(self):
        pass

class Copyable(ABC):
    @abstractmethod
    def copydoc(self):
        pass

class NetworkPrinter(Printable, Scanable, Copyable):
    def print(self):
        print("I can print")

    def scan(self):
        print("I can scan")

    def copydoc(self):
        print("I can make documents copy")

class Printer(Printable):
    def print(self):
        print("It's just a printer")

class Scanner(Scanable):
    def scan(self):
        print("It's just a scanner")

printer = Printer()
scanner = Scanner()
network_multi_mach = NetworkPrinter()

printer.print()
scanner.scan()
network_multi_mach.copydoc()