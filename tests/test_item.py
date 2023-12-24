"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 100)
item2 = Item("Ноутбук", 20000, 50)
item1.pay_rate = 0.85
item2.pay_rate = 0.85


def test_item_str():
    assert item1.__str__() == 'Смартфон'


def test_calculation():
    assert Item.calculate_total_price(item1) == 1000000
    assert Item.calculate_total_price(item2) == 1000000


def test_discount():
    assert Item.apply_discount(item1) == 8500
    assert Item.apply_discount(item2) == 17000




