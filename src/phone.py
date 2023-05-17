from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        elif isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError(f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")

    # @property
    # def number_of_sim(self):
    #     return self.__number_of_sim
    #
    # @number_of_sim.setter
    # def number_of_sim(self, number_of_sim):
    #     if number_of_sim > 0:
    #         self.__number_of_sim = number_of_sim
    #     else:
    #         raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
