# Section 22: Handling Exceptions with Try-Except in Python

In Python, exceptions are events that occur during the execution of a program that disrupt the normal flow of
instructions. These can be errors, warnings, or other exceptional conditions. Python provides the `try-except` block to
handle exceptions and gracefully respond to them, preventing the program from crashing. Let's explore how to
use `try-except` effectively:

## The Try-Except Block

The `try-except` block allows you to handle exceptions by attempting a piece of code and providing an alternative action
if an exception occurs.

### Example

```python
try:
    result = 10 / 0  # Attempting a division by zero
    print("Result:", result)  # This will not be executed if an exception occurs
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

In this example, we attempt to divide by zero, which would normally raise a ZeroDivisionError. However, we catch this
error using the except block and print a custom error message instead.

## Handling Multiple Exceptions

You can handle multiple types of exceptions using multiple except blocks.

```python
try:
    result = 10 / 0  # Attempting a division by zero
    print("Result:", result)  # This will not be executed if an exception occurs
except ZeroDivisionError:
    print("Cannot divide by zero!")
except TypeError:
    print("Invalid operation!")
```

In this example, we handle both `ZeroDivisionError` and `TypeError` exceptions.

## Handling All Exceptions

You can use a generic `except` block to handle any type of exception.

```python
try:
    result = 10 / 0  # Attempting a division by zero
    print("Result:", result)  # This will not be executed if an exception occurs
except Exception as e:
    print("An exception occurred:", str(e))
```

In this example, we use `Exception` to catch any type of exception. The exception message is printed using `str(e)`.

## The Finally Block

You can use the `finally` block to execute code regardless of whether an exception was raised or not.

```python
try:
    result = 10 / 0  # Attempting a division by zero
    print("Result:", result)  # This will not be executed if an exception occurs
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed, regardless of exceptions.")
```

In this example, the `finally` block ensures that the message is always printed.

## Summary

The `try-except` block is a powerful feature in Python that allows you to handle exceptions and gracefully respond to
errors or exceptional conditions in your code. Understanding how to use `try-except` effectively enhances the robustness
and reliability of your programs.

### [Handling exceptions exercises][1]
### [Section 23: Understanding Methods in Python Classes][2]

[1]: ../python_exercises/22_handling_exceptions.py
[2]: ./23_class_methods.md
