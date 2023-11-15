# Section 13: Parameters in Functions and Methods

Parameters in functions and methods allow you to pass data into the function or method to perform operations on. They
make functions and methods more flexible and versatile by enabling them to handle different inputs. Let's explore how
parameters work in functions and methods:

## Parameters in Functions

Parameters in functions are variables that are defined inside the parentheses of a function's definition. They act as
placeholders for the actual values that will be passed to the function when it's called.

### Function with Parameters

```python
def greet(name):
    return f"Hello, {name}!"
```

In this example, `name` is a parameter of the `greet` function. It acts as a placeholder for the actual name that will
be provided when the function is called.

### Function Call with Arguments

```python
message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

In this function call, the value "Alice" is passed as an argument to the `greet` function, and it gets assigned to
the `name` parameter inside the function.

## Parameters in Methods

Parameters in methods work similarly to parameters in functions but are defined within a class's method. They allow
methods to accept data specific to the instance of the class.

### Method with Parameters

```python
class Calculator:
    def add(self, a, b):
        return a + b
```

In this example, the `add` method accepts two parameters, `a` and `b`.

### Method Call with Arguments

```python
calculator = Calculator()
result = calculator.add(3, 5)
print(result)  # Output: 8
```

In this method call, the values 3 and 5 are passed as arguments to the `add` method, and they get assigned to the `a`
and `b` parameters inside the method.

## Default Parameters

In Python, you can assign default values to parameters. These default values are used when the caller doesn't provide a
value for that parameter.

```python
def greet(name="User"):
    return f"Hello, {name}!"
```

In this example, if no `name` is provided when calling `greet`, it defaults to "User".

## Sumary

Parameters allow you to make your functions and methods more versatile by accepting different inputs. They are
placeholders for actual data that will be passed to functions and methods when they are called. Understanding how to use
parameters effectively is crucial for creating flexible and reusable code.

### [parameters exercises][1]
### [Section 14: Understanding *args in Python Functions][2]


[1]: ../python_exercises/13_parameters_in_functions_and_methods.py
[2]: ./14_args.md