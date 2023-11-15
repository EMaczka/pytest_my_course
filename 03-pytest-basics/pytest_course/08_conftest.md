# Section 8: conftest in Pytest

The `conftest.py` file is a key component in organizing and configuring tests in a Pytest project. It allows you to
define fixtures, hooks, and other configurations that are shared across multiple test files.

## Fixture Sharing

Fixtures defined in conftest.py are automatically discovered by Pytest and made available to all test files in the same
directory and subdirectories. This allows for easy sharing of common setup code among tests.

## Fixture Scope in `conftest.py`

You can set the scope of fixtures in `conftest.py` to determine how often a fixture is created. The available scopes
are:

* **function:** Fixture is called once per test function (default).
* **class:** Fixture is called once per test class.
* **module:** Fixture is called once per module.
* **session:** Fixture is called once per entire test session.

```python
import pytest


@pytest.fixture(scope="function")
def function_fixture():
    pass


@pytest.fixture(scope="class")
def class_fixture():
    pass


@pytest.fixture(scope="module")
def module_fixture():
    pass


@pytest.fixture(scope="session")
def session_fixture():
    pass
```

## Common Uses of `conftest.py`

* Sharing Fixtures Across Tests:

Define commonly used fixtures in `conftest.py` to share them across different test files.

* Configuration Settings:

Store configuration settings or constants in `conftest.py` to be used across the test suite.

* Plugin Initialization:

Initialize and configure plugins or custom hooks for your tests.

## Structure Example

A simple directory structure could look like this:

```lua
project_root/
|-- tests/
|   |-- conftest.py
|   |-- test_file1.py
|   |-- test_file2.py
|-- src/
|   |-- your_module.py
|-- conftest.py
|-- ...
```

* **project_root/tests/conftest.py:** Contains shared fixtures for the tests in the tests/ directory.
* **project_root/conftest.py:** Contains shared fixtures for the entire project.

## `conftest.py` Fixture Example

Here's an example of a fixture defined in `conftest.py`:

```python
import pytest


@pytest.fixture
def common_setup():
    # Perform common setup operations
    yield
    # Perform common teardown operations
```

This fixture can be utilized in any test file within the same directory and its subdirectories.

The `conftest.py` file is a powerful tool for managing shared configurations, fixtures, and other testing-related
functionalities across your Pytest project.


## Next task
### [Exercise 6: Usage of conftest.py][1]
### [Section 9: Understanding pytest.ini][2]

[1]: ../pytest_exercises/06_conftest.md
[2]: 09_pytest_ini.md