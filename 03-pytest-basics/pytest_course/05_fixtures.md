# Section 5: Fixtures in Pytest

In Pytest, fixtures are functions that create data or set up the environment needed for your tests. Fixtures provide a
way to initialize test resources and share them across multiple tests, improving code modularity and reducing
redundancy.

## Creating a Fixture

To create a fixture, use the `@pytest.fixture` decorator before a function. This function will be executed before the
tests that use it.

```python
import pytest


@pytest.fixture
def setup_data():
    data = "some initial data"
    return data
```

## Using a Fixture in a Test Function

To use a fixture in a test function, simply include the fixture name as a parameter in the test function. Pytest will
automatically call the fixture and pass the returned value to the test function.

```python
def test_example(setup_data):
    assert len(setup_data) == 15
```

## Fixture Scope

Fixtures can have different scopes:

* **function:** Default scope. The fixture is called once per test function.
* **class:** The fixture is called once for each test class.
* **module:** The fixture is called once per module.
* **session:** The fixture is called once per entire test session.

You can specify the `scope` by passing the scope parameter to `@pytest.fixture`.

```python
import pytest


@pytest.fixture(scope="module")
def setup_data_module():
    data = "some initial data for module"
    return data
```

## Using Multiple Fixtures

You can use multiple fixtures in a test by including their names as parameters in the test function.

```python
def test_multiple_fixtures(setup_data, setup_data_module):
    assert len(setup_data) < len(setup_data_module)
```

## Fixture Finalization (teardown)

You can add finalization steps (teardown) to a fixture by using the `yield` statement. Code after the `yield` will
execute after the test function that uses the fixture.

```python
import pytest


@pytest.fixture
def setup_and_teardown():
    print("Setup")
    yield
    print("Teardown")


def test_with_teardown(setup_and_teardown):
    print("Test")
```

In this example, "Setup" will be printed before the test, and "Teardown" will be printed after the test.

## Using Fixtures for Resource Cleanup

Fixtures can also be used for resource cleanup, ensuring resources are properly released after the test.

```python
import os
import tempfile
import pytest


@pytest.fixture
def temp_directory():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    os.rmdir(temp_dir)


def test_temp_directory(temp_directory):
    assert os.path.exists(temp_directory)
```

In this example, a temporary directory is created and cleaned up after the test.

Fixtures are a powerful feature in Pytest that enable better test organization, resource management, and test
environment setup.

## Next task

### [Exercise 2: Creating a Simple Fixture][1]
### [Exercise 3: Before and after fixture][2]
### [Section 6: Fixture parametrize][3]


[1]: ../pytest_exercises/02_fixture_usage.md
[2]: ../pytest_exercises/03_before_after_fixture.md
[3]: 06_fixture_parametrize.md