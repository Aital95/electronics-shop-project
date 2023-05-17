class LanguageMixin:
    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self


class Keyboard(LanguageMixin):
    def __init__(self, name, price, warranty):
        super().__init__()
        self.name = name
        self.price = price
        self.warranty = warranty

    def __str__(self):
        return self.name