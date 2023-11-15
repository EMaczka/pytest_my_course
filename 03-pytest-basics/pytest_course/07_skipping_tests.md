# Section 7: Skipping Tests in Pytest

There are different ways to skip tests in Pytest:

## Using the skip decorator:

You can use the `skip` decorator to skip a test unconditionally.

```python
import pytest


@pytest.mark.skip(reason="Test is not implemented yet")
def test_function_to_skip():
    assert 1 == 2
```

In this example, the test `test_function_to_skip` will be skipped with the reason specified.

## Conditionally Skipping Tests:

You can conditionally skip a test using an `if` statement combined with the `pytest.skip` function.

```python
import pytest


def test_conditionally_skip():
    if not some_condition:
        pytest.skip("Skipping this test due to some condition")
    assert 1 == 2
```

In this case, the test will only be skipped if the condition is met.

## Skipping Entire Test Classes:

You can also skip an entire test class by using the `pytest.mark.skip` decorator at the class level.

```python
import pytest


@pytest.mark.skip(reason="Skipping the entire class")
class TestSomeClass:
    def test_some_method(self):
        assert 1 == 2
```

All tests within the skipped class will be skipped.

## Skipping with Expressions:

You can use expressions to conditionally skip a test based on certain conditions.

```python
import pytest


@pytest.mark.skipif(condition, reason="Skipping this test based on condition")
def test_function_to_skip():
    assert 1 == 2
```

## Skipping on Certain Platforms:

You can skip a test based on the platform (e.g., operating system).

```python
import pytest
import sys


@pytest.mark.skipif(sys.platform != "win32", reason="Skipping on non-Windows platforms")
def test_windows_only_function():
# Test code for Windows only
```

## Skipping and Marking a Test as Expected to Fail:

You can mark a test as expected to fail using pytest.mark.xfail which allows the test to run but will be marked as
failed.

```python
import pytest


@pytest.mark.xfail(reason="This test is expected to fail")
def test_function_expected_to_fail():
    assert 1 == 2
```

In this case, the test will run, but it's marked as expected to fail.

By using these approaches, you can selectively skip tests in Pytest based on various conditions or scenarios.

## Next task
### [Exercise 5: Using pytest skip][1]
### [Section 8: conftest in Pytest][2]

[1]: ../pytest_exercises/05_skipping_test.md
[2]: 08_conftest.md
