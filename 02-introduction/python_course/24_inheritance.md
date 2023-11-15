# Section 24: Understanding Inheritance in Python

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit attributes and
methods from another class. The class that inherits is called a subclass or derived class, and the class being inherited
from is called a superclass or base class. Inheritance facilitates code reusability and promotes the creation of
hierarchical relationships among classes. Let's explore how to work with inheritance in Python:

## Defining a Simple Base Class

A base class is a class from which other classes inherit. It contains common attributes and methods that are shared
among its subclasses.

```python
class Animal:
    def speak(self):
        print("Animal speaking.")


# Creating an instance of the base class
animal = Animal()

# Calling a method of the base class
animal.speak()
```

In this example, `Animal` is a simple base class with a method `speak`.

## Creating a Subclass

A subclass inherits attributes and methods from its superclass. It can also have its own additional attributes and
methods.

```python
class Dog(Animal):
    def bark(self):
        print("Dog barking.")


# Creating an instance of the subclass
dog = Dog()

# Calling methods from both the superclass and subclass
dog.speak()  # Output: Animal speaking.
dog.bark()  # Output: Dog barking.
```

In this example, `Dog` is a subclass of `Animal`, inheriting the `speak` method from the base class and defining its own
method, `bark`.

## Overriding Methods

A subclass can override methods of its superclass by defining a method with the same name.

```python
class Cat(Animal):
    def speak(self):
        print("Cat meowing.")


# Creating an instance of the subclass
cat = Cat()

# Calling the overridden method
cat.speak()  # Output: Cat meowing.
```

In this example, the `Cat` subclass overrides the `speak` method defined in the base class.

## Calling the Superclass Method

A subclass can call a method from its superclass using the super() function.

```python
class Horse(Animal):
    def speak(self):
        super().speak()
        print("Horse neighing.")


# Creating an instance of the subclass
horse = Horse()

# Calling methods from both the superclass and subclass
horse.speak()
```

In this example, the `Horse` subclass calls the `speak` method from the base class using `super()` and then defines its
own behavior.

## Summary

Inheritance is a powerful concept in object-oriented programming that enables code reuse and the creation of
hierarchical relationships among classes. Understanding how to define and use base classes, subclasses, method
overriding, and calling superclass methods is essential for effective use of inheritance in Python.

### [Inheritances exercises][1]
### [Go back to main Readme][2]

[1]: ../python_exercises/24_inheritances.py
[2]: ../../README.md

