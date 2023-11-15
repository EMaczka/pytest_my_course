# Section 2: Variables in Python

Variables are essential components in programming that allow you to store and manage data within a program. In Python,
variables are used to represent and store various types of information. Let's explore variables in more detail:

## Declaring Variables

In Python, declaring a variable is as simple as choosing a name and assigning a value to it using the assignment
operator (`=`). For example:

```python
name = "Alice"
age = 30
```

In the above code, we've declared two variables: name and age. The name variable stores a string, and the age variable
stores an integer.

## Variable Naming Rules

When naming variables in Python, follow these rules:

* Variable names must start with a letter (a-z, A-Z) or an underscore (_).
* Variable names can contain letters, numbers, and underscores.
* Variable names are case-sensitive, meaning name and Name are considered different variables.

Avoid using Python keywords (e.g., if, while, for, print) as variable names.

## Variable Assignment

You can change the value of a variable after it's been assigned. For example:

```python
age = 30  # Assigning 30 to 'age'
age = 31  # Reassigning 'age' to 31
```

## Data Types and Variables

Variables in Python are dynamic, which means their data type can change during execution. Python automatically
determines the data type based on the assigned value. For example:

```python
x = 42  # 'x' is an integer
x = "Hello"  # 'x' is a string now
x = 3.14  # 'x' is a floating-point number
```

## Variable Scope

The scope of a variable defines where it can be accessed or used within your code. In Python, variables can have global
or local scope. A global variable can be accessed from anywhere in your code, while a local variable is confined to a
specific block or function.

## Summary
Understanding variables and how to use them is fundamental to programming in Python. They allow you to store and
manipulate data, making your code more flexible and dynamic. Proper naming and management of variables are essential for
writing clean and maintainable code.

### [variables exercises][1]
### [Section 3: Data Types in Python][2]


[1]: ../python_exercises/02_variables.py
[2]: ./03_datatypes.md
