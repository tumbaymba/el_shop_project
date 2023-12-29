import csv
import os


class Item:
    """
    Класс для представления товара в магазине
    """
    pay_rate = 0.85
    all = []
    file = "../items.csv"

    def __init__(self, name: str, price: float, quantity: int):
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    @classmethod
    def instantiate_from_csv(cls, s):
        with open(os.path.join(os.path.dirname(__file__), 'items.csv'), 'r', newline='') as csvfile:
            data = csv.DictReader(csvfile)
            product: dict
            for product in data:
                cls(product['name'], cls.string_to_number(product['price']), cls.string_to_number(product['quantity']))

    @staticmethod
    def string_to_number(number: str) -> int:
        return int(float(number))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        elif len(name) > 10:
            print("Количество букв в наименовании больше 10")

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
