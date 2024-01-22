import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120000, 5, 2)


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_str(phone):
    assert str(phone) == "iPhone 14"


def test_repr(phone):
    assert str(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(phone):
    assert phone.number_of_sim == 2


def test_error_number_of_sim(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = -1


def test_add(phone, item):
    assert phone + item == 25
    assert phone + phone == 10
