# Section 7: Logical Operators in Python

Logical operators in Python are used to perform logical operations on Boolean values. These operators allow you to
combine and manipulate Boolean values to make decisions and control the flow of your program. Let's explore the common
logical operators:

## Logical AND (and)

The logical AND operator (`and`) returns `True` if both operands are `True`, and `False` otherwise. For example:

```python
x = True
y = False

result = x and y  # 'result' is False because both 'x' and 'y' are not True
```

## Logical OR (or)

The logical OR operator (or) returns True if at least one of the operands is True, and False if both are False. For
example:

```python
x = True
y = False

result = x or y  # 'result' is True because 'x' is True
```

## Logical NOT (not)

The logical NOT operator (not) is used to reverse the logical value of its operand. It returns True if the operand is
False and False if the operand is True. For example:

```python
x = True

result = not x  # 'result' is False because 'x' is True, but we're negating it
```

## Combining Logical Operators

You can combine logical operators to create more complex conditions. For example:

```python
x = True
y = False
z = True

result = x and (not y) or z  # 'result' is True because 'x' is True, 'not y' is True, and 'z' is True
```

## Sumary

Logical operators are fundamental for making decisions and controlling the flow of your Python programs. They allow you
to create conditions that depend on multiple Boolean values and determine the logical outcomes. Understanding how to use
logical operators is crucial for writing effective and logical code.

### [logical operators exercises][1]
### [Section 08: Logical Operators and Comparisons in Python][2]


[1]: ../python_exercises/07_logical_operators.py
[2]: ./08_logical_and_comparision_operators.md

