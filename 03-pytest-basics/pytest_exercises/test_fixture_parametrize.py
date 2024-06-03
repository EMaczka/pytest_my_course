import pytest


def test_print_hello():
    var = "Hello!"
    print(var)


@pytest.mark.parametrize("test", ["text"])
def test_print_2(test):
    print(test)


@pytest.mark.parametrize("test1, test2", [("text1", "text2")])
def test_print_3(test1, test2):
    print(test1, test2)
