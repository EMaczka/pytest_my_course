# Section 15: Understanding `**kwargs` in Python Functions

In Python, `**kwargs` is a special syntax used in function definitions to pass a variable number of keyword arguments.
It allows a function to accept any number of keyword arguments, making the function more flexible and versatile. Let's
explore how `**kwargs` works and how to use it:

## Using `**kwargs` in Function Definitions

The `**kwargs` syntax is used to pass a variable number of keyword arguments to a function. It collects these arguments
into a dictionary, where the keys are the parameter names and the values are the corresponding values passed to the
function.

### Example

```python
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


greet(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
```

In this example, the `greet` function uses `**kwargs` to accept any number of keyword arguments. Inside the function, we
loop through the `kwargs` dictionary and print the key-value pairs.

### Using **kwargs with Other Parameters

You can use `**kwargs` along with regular parameters and `*args` in a function. However, `*args` must come
before `**kwargs`.

```python
def print_info(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info("Alice", "Bob", age=30, city="New York")
# Output:
# Alice
# Bob
# age: 30
# city: New York
```

In this example, the `print_info` function uses both `*args` and `**kwargs` to accept a variable number of positional
and keyword arguments. We then print the positional arguments and the key-value pairs.

## Summary

`**kwargs` is a powerful feature in Python that allows functions to accept a variable number of keyword arguments. It's
useful when you want to pass a flexible set of named parameters to a function. Understanding how to use `**kwargs` can
greatly enhance the versatility and functionality of your functions.

### [**kwargs exercises][1]
### [Section 16: Default Parameter Values in Python Functions][2]


[1]: ../python_exercises/15_kwargs.py
[2]: ./16_default_parameter_values_in_functions.md

