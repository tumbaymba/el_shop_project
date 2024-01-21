from src.item import Item


class Mix_lang():
    lang_count = 0

    def __init__(self):
        self._language = "EN"

    @property
    def language(self):
        return self._language

    def language(self, value):
        if value == "RU" or value == "EN":
            return self._language

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
        return self


class Keyboard(Item, Mix_lang):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        Mix_lang.__init__(self)
