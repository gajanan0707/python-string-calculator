import pytest
from string_calculator import add

def test_add_empty_string():
    assert add("") == 0

def test_add_single_number():
    assert add("1") == 1

def test_add_two_numbers():
    assert add("1,5") == 6

def test_add_multiple_numbers():
    assert add("1,2,3,4,5") == 15

def test_add_newlines_between_numbers():
    assert add("1\n2,3") == 6
    assert add("1,2\n3") == 6

def test_custom_delimiter():
    assert add("//;\n1;2") == 3
    assert add("//|\n1|2|3") == 6
    assert add("//sep\n1sep2sep3") == 6

def test_negative_numbers():
    with pytest.raises(ValueError) as exc:
        add("-1,2")
    assert str(exc.value) == "negative numbers not allowed: -1"

    with pytest.raises(ValueError) as exc:
        add("2,-4,3,-5")
    assert str(exc.value) == "negative numbers not allowed: -4, -5" 