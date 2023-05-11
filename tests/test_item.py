"""Здесь надо написать тесты с использованием pytest для модуля item."""
import os
import csv
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


def test_instantiate_from_csv():
    with open('test_items.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'price', 'quantity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'name': 'Телефон', 'price': '500', 'quantity': '10'})
        writer.writerow({'name': 'Наушники', 'price': '100', 'quantity': '20'})

    Item.instantiate_from_csv()

    assert len(Item.all) == 2
    assert Item.all[0].name == 'Телефон'
    assert Item.all[0].price == 500.0
    assert Item.all[0].quantity == 10
    assert Item.all[1].name == 'Наушники'
    assert Item.all[1].price == 100.0
    assert Item.all[1].quantity == 20

    os.remove('test_items.csv')


def test_string_to_number():
    assert Item.string_to_number('123') == 123
    assert Item.string_to_number('3.14') == 3.14
    assert Item.string_to_number('-50') == -50
    assert Item.string_to_number('invalid') is None
    assert isinstance(Item.string_to_number('123'), int)
    assert isinstance(Item.string_to_number('3.14'), float)
    assert isinstance(Item.string_to_number('-50'), int)


def test_repr():
    item = Item('Телефон', 500, 10)
    assert repr(item) == "Item('Телефон', 500, 10)"


def test_str_method():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'



