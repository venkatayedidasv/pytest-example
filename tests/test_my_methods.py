import pytest
from src.my_methods import add_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(10, 5) == 15
    assert add_numbers(-1, 1) == 0

