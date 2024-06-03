import pytest
import sqlite3


@pytest.fixture
def setup():
    print("Performing setup before test.")


@pytest.fixture
def teardown():
    print("Performing teardown after test.")


@pytest.fixture
def setup_and_teardown():
    conn = sqlite3.connect(":memory")
    print("Connection setup.")
    yield
    conn.close()
    print("Connection terminated.")
