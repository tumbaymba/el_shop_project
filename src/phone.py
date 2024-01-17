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

        if value >= 0:
            self._number_of_sim = value
        else:
            raise ValueError("Количество SIM- карт должно быть целым числом и больше 0.")


