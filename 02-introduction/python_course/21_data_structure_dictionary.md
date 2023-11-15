# Section 21: Understanding Dictionaries in Python

Dictionaries are a fundamental data structure in Python used to store collections of key-value pairs. Each key in a
dictionary maps to a value, making it easy to look up values based on their associated keys. Dictionaries are unordered
and mutable, allowing you to modify, add, and remove key-value pairs. Let's explore how dictionaries work and how to use
them effectively:

## Creating a Dictionary

A dictionary is created by enclosing key-value pairs within curly braces `{}`, with each pair separated by commas.

### Example

```python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
```

In this example, `my_dict` is a dictionary containing three key-value pairs.

## Accessing Values

Values in a dictionary are accessed by their corresponding keys.

```python
my_dict = {"name": "Alice", "age": 30}

print(my_dict["name"])  # Output: Alice
print(my_dict["age"])  # Output: 30
```

## Modifying a Dictionary

Dictionaries are mutable, meaning you can change the values associated with a key, add new key-value pairs, and remove
key-value pairs.

```python
my_dict = {"name": "Alice", "age": 30}

my_dict["age"] = 31  # Update a value
my_dict["city"] = "New York"  # Add a new key-value pair
del my_dict["name"]  # Remove a key-value pair

print(my_dict)  # Output: {'age': 31, 'city': 'New York'}
```

## Dictionary Methods

Dictionaries have built-in methods for various operations, including getting keys (`keys()`), getting values (`values()`),
getting key-value pairs (`items()`), and more.

```python
my_dict = {"name": "Alice", "age": 30}

keys_list = list(my_dict.keys())  # Get keys as a list
values_list = list(my_dict.values())  # Get values as a list
items_list = list(my_dict.items())  # Get key-value pairs as a list of tuples

print(keys_list)  # Output: ['name', 'age']
print(values_list)  # Output: ['Alice', 30]
print(items_list)  # Output: [('name', 'Alice'), ('age', 30)]
```

## Summary

Dictionaries are versatile and widely used data structures in Python that allow you to store and access values based on
associated keys. Understanding how to create, access, modify, and perform operations on dictionaries is essential for
effective programming in Python.

### [data structure dictionaries exercises][1]
### [Section 22: Handling Exceptions with Try-Except in Python][2]

[1]: ../python_exercises/21_data_structure_dictionary.py
[2]: ./22_handling_exceptions.md
