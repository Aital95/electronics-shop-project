"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount():
    Item.pay_rate = 0.8

    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    item1.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 20000


# from src.item import Item
#
#
# def test_get_total_price():
#     item = Item("Test item", 10.0, 5)
#     assert item.get_total_price() == 50.0
#
#
# def test_apply_discount():
#     item = Item("Test item", 10.0, 5)
#     item.apply_discount(0.2)  # apply 20% discount
#     assert item.price == 8.0
#     assert item.discount_level == 0.2
#
#
# def test_apply_discount_invalid(pytest=None):
#     item = Item("Test item", 10.0, 5)
#     with pytest.raises(ValueError):
#         item.apply_discount(1.5)
