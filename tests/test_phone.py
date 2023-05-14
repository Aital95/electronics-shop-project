from src.phone import Phone
from src.item import Item

def test_phone_addition():
    p1 = Phone("iPhone", 999, "The best phone", 10, 2)
    p2 = Phone("Samsung", 899, "Great phone too", 5, 1)
    p3 = p1 + p2
    assert p3.name == "iPhone Samsung"
    assert p3.price == 1898
    assert p3.description == "The best phone Great phone too"
    assert p3.quantity == 15
    assert p3.supported_sim_cards == 3

def test_phone_item_addition():
    p1 = Phone("iPhone", 999, "The best phone", 10, 2)
    i1 = Item("Screen protector", 20, "Protects phone screen", 50)
    i2 = p1 + i1  # should raise TypeError