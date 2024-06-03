# Section 4: Assertions in Pytest

Assertions in Pytest are statements that verify the correctness of the code being tested. They are used to validate
whether the actual results match the expected results. If the assertion evaluates to `True`, the test passes. If it's
`False`, the test fails.

## Basic Assertions

`assert`

The most basic assertion. It raises an exception if the given expression is `False`.

```python
def test_basic_assertion():
    assert 2 + 2 == 4
```

`assert condition, message`

You can include a custom message to provide more context when an assertion fails.

```python
def test_assertion_with_message():
    x = 5
    assert x > 10, "x should be greater than 10"
```

## Comparison Assertions

* `assert a == b` Asserts that a is equal to b.
* `assert a != b` Asserts that a is not equal to b.
* `assert a < b` Asserts that a is less than b.
* `assert a > b` Asserts that a is greater than b.
* `assert a <= b` Asserts that a is less than or equal to b.
* `assert a >= b` Asserts that a is greater than or equal to b.

## Other Common Assertions

`assert item in container`
Asserts that `item` is in `container`.

```python
def test_item_in_list():
    assert 2 in [1, 2, 3]
```

`assert item not in container`
Asserts that `item` is not in `container`.

```python
def test_item_not_in_list():
    assert 5 not in [1, 2, 3]
```

`assert condition is True`
Asserts that condition is True.

```python
def test_assert_true():
    assert 5 > 3 is True
```

`assert condition is False`
Asserts that `condition` is `False`.

```python
def test_assert_false():
    assert 5 < 3 is False
```

## Using `assert` with Functions

Assertions can be used with functions that return values for validation.

```python
def add(a, b):
    return a + b


def test_addition():
    result = add(2, 3)
    assert result == 5
```

## Handling Exceptions

`with pytest.raises(ExceptionType)`
Asserts that a specific exception is raised.

```python
def test_exception():
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0
```

These are some common assertion techniques in Pytest that you can use to validate your code during testing.


## Next task
### [Section 5: Fixtures in Pytest][1]

[1]: 05_fixtures.md
