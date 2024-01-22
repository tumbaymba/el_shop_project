import pytest
import csv
from config import ITEMS_PATH, BAD_PATH, BROKEN_FILE
from src.item import Item, InstantiateCSVError

@pytest.fixture
def item():
    return Item("Смартфон", 10000, 100)

def test_item_str(item):
    assert str(item) == 'Смартфон'


def test_calculation(item):
    assert item.calculate_total_price() == 1000000


def test_discount(item):
    assert item.apply_discount() == 8500.0


def test_repr(item):
    assert repr(item) == f"Item('Смартфон', 10000, 100)"


def test_name_setter(item):
    item.name = "Новое имя"
    assert item.name == "Новое имя"
    with pytest.raises(ValueError):
        item.name = "Оооооочень длиннноое название"


def test_instantiate_from_csv():
    Item.instantiate_from_csv(ITEMS_PATH)
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[2].price == 10.0
    assert Item.all[3].quantity == 5


def test_string_to_number_static():
    assert Item.string_to_number("5.65") == 5


def test_if_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(BAD_PATH)


def test_if_file_bad():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(BROKEN_FILE)