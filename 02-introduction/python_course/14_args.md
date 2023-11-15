# Section 14: Understanding `*args` in Python Functions

In Python, `*args` is a special syntax used in function definitions to pass a variable number of positional arguments.
It allows a function to accept any number of arguments, making the function more flexible and versatile. Let's explore
how `*args` works and how to use it:

## Using `*args` in Function Definitions

The `*args` syntax is used to pass a variable number of positional arguments to a function. It collects these arguments
into a tuple, which can be accessed within the function.

```python
def add(*args):
    result = 0
    for num in args:
        result += num
    return result


sum_result = add(1, 2, 3, 4, 5)
print(sum_result)  # Output: 15
```

In this example, the `add` function uses `*args` to accept any number of arguments. Inside the function, we loop
through the `args` tuple and sum up the values.

## Using *args with Other Parameters

You can use `*args` along with regular parameters in a function. However, `*args` must come after the regular
parameters.

```python
def greet(greeting, *args):
    for name in args:
        print(f"{greeting}, {name}!")


greet("Hello", "Alice", "Bob", "Charlie")

# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

In this example, the `greet` function has a regular parameter `greeting` and uses `*args` to accept additional names.
The function prints a greeting for each name provided.

## Sumary

`*args` is a powerful feature in Python that allows functions to accept a variable number of positional arguments. It's
useful when you don't know in advance how many arguments will be passed to a function. Understanding how to use `*args`
can enhance the flexibility and functionality of your functions.

### [*args exercises][1]
### [Section 15: Understanding **kwargs in Python Functions][2]


[1]: ../python_exercises/14_args.py
[2]: ./15_kwargs.md

