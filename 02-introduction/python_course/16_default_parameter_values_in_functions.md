# Section 16: Default Parameter Values in Python Functions

Default parameter values in Python functions allow you to set a default value for a function parameter. If the caller
doesn't provide a value for that parameter, the default value will be used. This makes functions more flexible and
convenient to use. Let's explore how to use default parameter values in Python functions:

## Using Default Parameter Values

You can specify default values for parameters in a function by assigning a value to the parameter in the function
definition.

```python
def greet(name="User"):
    return f"Hello, {name}!"
```

In this example, the `greet` function has a default parameter value of "User" for the `name` parameter. If the caller
doesn't provide a name, "User" will be used.

## Function Call

```python
message = greet("Alice")
print(message)  # Output: Hello, Alice!

default_message = greet()  # Using the default value
print(default_message)  # Output: Hello, User!
```

In the first function call, we provide a specific name, "Alice". In the second call, we don't provide any name, so the
default value, "User", is used.

## Combining Default and Non-Default Parameters

You can have parameters with default values alongside parameters without default values in the same function.

```python
def greet(greeting, name="User"):
    return f"{greeting}, {name}!"
```

In this example, the `greet` function has both a parameter `greeting` without a default value and a parameter `name`
with a default value.

## Function Call

```python
message1 = greet("Hello", "Alice")
print(message1)  # Output: Hello, Alice!

message2 = greet("Hi")
print(message2)  # Output: Hi, User!
```

In the first function call, we provide values for both parameters. In the second call, we only provide a value for
the `greeting` parameter, and the default value for `name` is used.

## Summary

Default parameter values in Python functions provide a convenient way to set default behavior for a function. This makes
functions more flexible and allows them to handle a variety of use cases. Understanding how to use default parameter
values effectively is essential for creating versatile and user-friendly functions.

### [default parameters exercises][1]
### [Section 17: Understanding the "None" Object in Python][2]


[1]: ../python_exercises/16_default_parameter_values_in_functions.py
[2]: ./17_none_object.md
