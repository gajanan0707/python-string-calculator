import pytest
from string_calculator import add

def test_add_empty_string():
    assert add("") == 0

def test_add_single_number():
    assert add("1") == 1 