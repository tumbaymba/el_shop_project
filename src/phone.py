from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:

        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self) -> str:

        return f"{self.__class__.__name__}('{self.name}', " \
               f"{self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self) -> int:

        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int) -> None:

        if value <= 0:
            raise ValueError('Количество симкарт должно быть больше нуля.')
        self._number_of_sim = value

    def __add__(self, other) -> int | None:

        if issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        return None
