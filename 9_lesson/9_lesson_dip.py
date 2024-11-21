"""
Завдання 5: Принцип залежностей (Dependency Inversion Principle - DIP)

Використовуючи принцип DIP, переробіть код залежностей у вашому проекті так, щоб він використовував
абстракції та інтерфейси замість конкретних реалізацій. Переконайтеся, що класи залежностей
 не знають про конкретну реалізацію інших класів.
"""

from abc import ABC, abstractmethod

class DeliveryService(ABC):
    @abstractmethod
    def delivery(self, order):
        pass

class NovaPost(DeliveryService):
    def delivery(self, order):
        print(f"This is novapost")

class UkrPost(DeliveryService):
    def delivery(self, order):
        print(f"This is ukrpost")

class OrderProcess:
    def __init__(self, delivery_service):
        self.delivery_service = delivery_service

    def process_order(self, order):
        self.delivery_service.delivery(order)