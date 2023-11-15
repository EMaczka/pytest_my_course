# Section 23: Understanding Methods in Python Classes

In object-oriented programming (OOP), a method is a function associated with a class. Methods are defined within a class
and represent the behaviors or actions that instances of the class can perform. Understanding how to define and use
methods is crucial for effective programming in Python. Let's explore how to work with methods in Python classes:

## Defining Methods in a Class

Methods are defined within a class using the `def` keyword, just like regular functions. However, they are indented
within the class definition.

```python
class MyClass:
    def my_method(self):
        print("This is a method.")


# Creating an instance of the class
my_instance = MyClass()

# Calling the method
my_instance.my_method()
```

In this example, `my_method` is a method defined within the `MyClass` class. The `self` parameter is used to reference
the instance of the class within the method.

## Accessing Instance Variables

Methods can access and modify instance variables (attributes) of the class using self.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value


# Creating an instance with an initial value
my_instance = MyClass(42)

# Accessing and modifying the instance variable
print(my_instance.get_value())  # Output: 42
my_instance.set_value(100)
print(my_instance.get_value())  # Output: 100
```

In this example, `get_value` and `set_value` are methods that access and modify the value instance variable using `self`
.

Method Types
There are three main types of methods in Python classes:

* Instance Methods: These methods have access to instance variables and are the most common type of method.
* Class Methods: These methods have access to class variables and are denoted with the `@classmethod` decorator.
* Static Methods: These methods do not depend on instance or class state and are denoted with the `@staticmethod`
  decorator.

## Example of Class and Static Methods

```python
class MyClass:
    class_variable = 10

    def __init__(self, value):
        self.value = value

    def instance_method(self):
        return self.value * self.class_variable

    @classmethod
    def class_method(cls):
        return cls.class_variable

    @staticmethod
    def static_method():
        return "This is a static method."


# Creating an instance of the class
my_instance = MyClass(5)

# Accessing different types of methods
print(my_instance.instance_method())  # Output: 50
print(MyClass.class_method())  # Output: 10
print(MyClass.static_method())  # Output: This is a static method.
```

In this example, we demonstrate instance, class, and static methods and how they can be accessed.

## Summary

Methods are essential in Python classes, providing behaviors or actions that instances of the class can perform.
Understanding how to define, access, and use methods is crucial for effective object-oriented programming in Python.

### [Class methods exercises][1]
### [Section 24: Understanding Inheritance in Python][2]

[1]: ../python_exercises/23_class_methods.py
[2]: ./24_inheritance.md
