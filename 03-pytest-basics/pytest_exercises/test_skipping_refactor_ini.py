import pytest
import logging


@pytest.mark.skipif(reason="2.")
def test_print_first_variable():
    var = "first"
    print(var)


def test_print_second_variable(setup_before_session):
    logging.info("Second variable")
