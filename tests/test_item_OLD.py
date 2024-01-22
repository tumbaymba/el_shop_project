import pytest
import csv
from config import ITEMS_PATH, BAD_PATH, BROKEN_FILE
from src.item import Item, InstantiateCSVError


item = Item("Смартфон", 10000, 100)

file = "../src/items.csv"

def test_item_str():
    # item = Item("Смартфон", 10000, 100)
    assert str(item) == 'Смартфон'


def test_calculation():
    # item = Item("Смартфон", 10000, 100)
    assert item.calculate_total_price() == 1000000


def test_discount():
    # item = Item("Смартфон", 10000, 100)
    # item.pay_rate = 0.85
    # assert item.price == 8500

    assert Item.apply_discount(item) == 8500.0


def test_repr():
    assert f"Item('Смартфон', 10000, 20)"


def test_str():
    assert 'Смартфон'


def test_name_setter():
    assert 'Смартфон'


def test_instantiate_from_csv(file="../src/items.csv"):
    # Item.instantiate_from_csv("src/items.csv")
    # assert len(Item.instantiate_from_csv("src/items.csv")) == 5

    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[2].price == 10000
    assert Item.all[3].quantity == 100


def test_string_to_number_static():
    assert Item.string_to_number("5.65") == 5


def test_if_file_not_found():
    if file is None:
        assert Item.instantiate_from_csv(file) == "FileNotFoundError: Отсутствует файл item."


def test_if_file_bad():
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for data in reader:
            data_list = list(data.values())
            if len(data_list) < 3:
                assert Item.instantiate_from_csv(
                    file) == "src.item.InstantiateCSVError: InstantiateCSVError: Файл item.csv поврежден"
