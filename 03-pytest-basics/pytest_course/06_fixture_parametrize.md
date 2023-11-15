# Section 6: Fixture parametrize

`pytest.mark.parametrize` is a decorator that allows you to define and run multiple test cases within a single test
function. It's a convenient way to test a function with various inputs and expected outputs.

## Basic Usage

Here's how you can use `pytest.mark.parametrize` to run a test with multiple input-output combinations:

```python
import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize("a, b, expected_result", [
    (2, 3, 5),  # Test case 1
    (-1, 1, 0),  # Test case 2
    (0, 0, 0)  # Test case 3
])
def test_addition(a, b, expected_result):
    assert add(a, b) == expected_result
```

In this example, the `test_addition` test function is decorated with `@pytest.mark.parametrize`. The decorator takes
three arguments:

* `a`, `b`: Parameters for the test function.
* `expected_result`: The expected result of the addition.

The `test_addition` function will be called three times, once for each set of input parameters defined in the list.

## Handling Multiple Parameters

You can use multiple parameters in `@pytest.mark.parametrize` to test functions that take more than two inputs.

```python
@pytest.mark.parametrize("a, b, expected_result", [
    (2, 3, 5),  # Test case 1
    (-1, 1, 0),  # Test case 2
    (0, 0, 0),  # Test case 3
    (10, -5, 5)  # Test case 4
])
def test_addition(a, b, expected_result):
    assert add(a, b) == expected_result
```

## Naming Parameters

You can provide a custom name for the test cases by including it in the tuple along with the parameters.

```python
@pytest.mark.parametrize("a, b, expected_result", [
    (2, 3, 5),  # Test case: a=2, b=3
    (-1, 1, 0),  # Test case: a=-1, b=1
    (0, 0, 0),  # Test case: a=0, b=0
    pytest.param(10, -5, 5, marks=pytest.mark.xfail)  # Expected to fail
])
def test_addition(a, b, expected_result):
    assert add(a, b) == expected_result
```

## Marking Test Cases

You can use Pytest markers (like `pytest.mark.skip`, `pytest.mark.xfail`, etc.) to mark specific test cases.

```python
@pytest.mark.parametrize("a, b, expected_result", [
    (2, 3, 5),  # Test case 1
    (-1, 1, 0),  # Test case 2
    (0, 0, 0),  # Test case 3
    pytest.param(10, -5, 5, marks=pytest.mark.xfail)  # Expected to fail
])
def test_addition(a, b, expected_result):
    assert add(a, b) == expected_result
```

In this example, the fourth test case is marked as expected to fail using `pytest.mark.xfail`.

`pytest.mark.parametrize` is a powerful tool for writing concise and readable test cases with multiple input
combinations.

## Next task
### [Exercise 4: Usage of pytest parametrize][1]
### [Section 7: Skipping Tests in Pytest][2]

[1]: ../pytest_exercises/04_fixture_parametrize.md
[2]: 07_skipping_tests.md