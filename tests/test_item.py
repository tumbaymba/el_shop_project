"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_item_str():
    item = Item("Смартфон", 10000, 100)
    assert str(item) == 'Смартфон'


def test_calculation():
    item = Item("Смартфон", 10000, 100)
    assert item.calculate_total_price() == 1000000


def test_discount():
    item = Item("Смартфон", 10000, 100)
    item.pay_rate = 0.85
    assert item.price == 8500


def test_repr(gadgets):
    assert f"Item('Смартфон', 10000, 100)"


def test_str(gadgets):
    assert 'Смартфон'

def test_name_setter(gadgets):
    gadgets.name = "Смартфон"
    assert gadgets.name == "Смартфон"


def test_instantiate_from_csv():
    Item.instantiate_from_csv('..items.csv')

    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[2].price == 10000
    assert Item.all[3].quantity == 100


def test_string_to_number_static():

    assert Item.string_to_number("5.65") == 5
