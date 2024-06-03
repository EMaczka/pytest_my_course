import pytest


@pytest.fixture
def herbs():
    return ["thyme", "colander", "sea salt"]


def test_print_herbs(herbs):
    print(f"Herbs: {herbs}")
