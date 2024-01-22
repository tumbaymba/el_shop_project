from src.keyboard import Keyboard


values = Keyboard('Dark Project KD87A', 9600, 5)

def test_lang():
    assert str(values.language) == "EN"

def test_str():
    assert str(values) == "Dark Project KD87A"

def test_change_lang():
    values.change_lang()
    assert str(values.language) == "RU"
    values.change_lang()
    assert str(values.language) == "EN"
    values.change_lang().change_lang()
    assert str(values.language) == "EN"






