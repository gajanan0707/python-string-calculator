import pytest
from string_calculator import add

def test_add_empty_string():
    assert add("") == 0 