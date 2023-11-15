# Section 12: Functions and Methods in Python

Functions and methods are fundamental concepts in Python and programming in general. They allow you to group code into
reusable blocks, improving organization, reusability, and modularity in your code. Let's explore what functions and
methods are and how they are used:

## Functions

A function is a block of reusable code that performs a specific task or set of tasks. Functions are defined using
the `def` keyword followed by the function name and a set of parentheses. Parameters (input) can be passed into a
function, and the function can return a value as a result (output).

### Function Definition

```python
def greet(name):
    return f"Hello, {name}!"
```

Function Call

```python
message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

### Methods

Methods are similar to functions but are associated with specific objects or data types in Python. They are functions
that are defined within a class and can be used to modify the object's state or perform operations related to the
object.

### Method Definition

```python
class MyClass:
    def say_hello(self):
        print("Hello!")


# Creating an instance of MyClass
my_instance = MyClass()

# Calling the method
my_instance.say_hello()  # Output: Hello!
```

In this example, `say_hello` is a method of the `MyClass` class.

### Key Differences

* Functions are defined using the def keyword, while methods are defined within a class.
* Methods are associated with a specific object and can access and modify its state.
* Functions are stand-alone, while methods are defined within a class and typically operate on instance variables.

## Sumary

Functions and methods are crucial for code organization, reusability, and maintainability. Functions provide a way to
modularize code and perform specific tasks, while methods are functions associated with specific objects or data types,
allowing for more targeted actions.

### [function and methods exercises][1]
### [Section 13: Parameters in Functions and Methods][2]


[1]: ../python_exercises/12_functions_and_methods.py
[2]: ./13_parameters_in_functions_and_methods.md
