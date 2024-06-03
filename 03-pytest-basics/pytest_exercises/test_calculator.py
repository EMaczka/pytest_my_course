import pytest

from calculator import *


def test_add():
    assert 3 + 7 == 10
    assert 4.14 + 95.86 == 100
    assert 2 + 7.9 == 9.9


def test_invalid_arguments():
    with pytest.raises(TypeError):
        add(1, "Potter")
    with pytest.raises(TypeError):
        add("Harry", 3.14)
    with pytest.raises(TypeError):
        add(1, 2, 3)


def test_empty_list():
    assert sum_list([]) == 0

# pytest test_calculator.py
# pytest test_calculator.py::test_add
# pytest test_calculator.py::test_add test_calculator.py::test_invalid_arguments
