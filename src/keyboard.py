from src.item import Item


class LanguageMixin:
    def __init__(self, *args):
        super().__init__(*args)
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self


class Keyboard(LanguageMixin, Item):
    def __init__(self, name, price, warranty):
        super().__init__(name, price, warranty)
        self.name = name
        self.price = price
        self.warranty = warranty

    def __str__(self):
        return self.name
