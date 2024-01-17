from src.item import Item

class Mix_lang():
    lang_count = 0

    def __init__(self):
        self._language = "EN"

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value == "RU" or value == "EN":
            return self._language

    def change_lang(self):
        self.lang_count += 1
        if self.lang_count % 2 == 0:
            self._language = "EN"
            return self
        else:
            self._language = "RU"
            return self


class Keyboard(Item, Mix_lang):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        Mix_lang.__init__(self)
