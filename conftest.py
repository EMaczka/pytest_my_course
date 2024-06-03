import pytest


@pytest.fixture(scope="session")
def setup_before_session():
    print("Performing setup before session")
