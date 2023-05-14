import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.general_summ = self.price + self.quantity

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError(f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")

    def __str__(self):
        return self.name
    @property
    def name(self):
        """
        Геттер для получения значения приватного атрибута name.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Сеттер для установки значения приватного атрибута name.
        Проверяет, что длина наименования товара не больше 10 символов.
        """
        if len(name) <= 10:
            self.__name = name
        else:
            print("Имя не должно быть длиннее 10 символов")

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv.
        """
        with open('../src/items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all.clear()
            for row in reader:
                print(row)
                cls.all.append(cls(row['name'], int(row['price']), int(row['quantity'])))
        return len(cls.all)

    @staticmethod
    def string_to_number(number, default=None):
        """
        Статический метод, преобразующий строку в число.
        """
        try:
            return int(number)
        except ValueError:
            try:
                return float(number)
            except ValueError:
                return default
    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
