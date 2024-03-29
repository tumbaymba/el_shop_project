import csv


class Item:
    pay_rate = 0.85
    all = []


    def __init__(self, name: str, price: float, quantity: int):
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'


    @classmethod
    def instantiate_from_csv(cls, file="../src/items.csv") -> None:
        cls.all.clear()
        try:
            with open(file, 'r', encoding="windows-1251") as csvfile:

                data = csv.DictReader(csvfile)
                product: dict
                for product in data:
                    cls(
                        product['name'],
                        float(product['price']),
                        cls.string_to_number(product['quantity'])
                    )

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        except KeyError:
            raise InstantiateCSVError()


    @staticmethod
    def string_to_number(number: str) -> int:
        return int(float(number))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, len_name):
        if len(len_name) <= 10:
            self.__name = len_name
        elif len(len_name) > 10:
            raise ValueError("Количество букв в наименовании больше 10")


    def calculate_total_price(self):
        return self.price * self.quantity

    def __add__(self, other) -> int:
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return 0

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price


class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'InstantiateCSVError: Файл item.csv поврежден'

    def __str__(self):
        return self.message


