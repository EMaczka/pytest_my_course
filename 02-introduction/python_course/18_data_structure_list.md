# Section 18: Understanding Lists in Python

Lists are a fundamental data structure in Python used to store collections of items. A list can contain a variety of
data types, including numbers, strings, and even other lists. Lists are ordered, mutable, and allow duplicates. Let's
explore how lists work and how to use them effectively:

## Creating a List

A list is created by enclosing elements within square brackets `[]`, separated by commas.

```python
my_list = [1, "hello", 3.14, True]
```

In this example, `my_list` is a list containing four elements of different data types.

## Accessing Elements

Elements in a list are accessed by their index, starting from 0 for the first element.

```python
my_list = [10, 20, 30, 40]

print(my_list[0])  # Output: 10
print(my_list[2])  # Output: 30
```

## Modifying a List

Lists are mutable, meaning you can change the values of individual elements, append new elements, remove elements, and
more.

```python
my_list = [10, 20, 30]

my_list[1] = 25  # Update an element
my_list.append(40)  # Append an element
my_list.remove(10)  # Remove an element

print(my_list)  # Output: [25, 30, 40]
```

## List Operations

Lists support various operations, including concatenation (`+`), repetition (`*`), and finding the length (`len()`).

```python
list1 = [1, 2, 3]
list2 = [4, 5]

concatenated_list = list1 + list2
repeated_list = list1 * 3
list_length = len(list1)

print(concatenated_list)  # Output: [1, 2, 3, 4, 5]
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(list_length)  # Output: 3
```

## List Methods

Lists have built-in methods for various operations, such as adding elements (`append()`), removing elements (`remove()`)
, sorting (`sort()`), and more.

```python
my_list = [5, 2, 8, 1]

my_list.append(4)  # Add an element
my_list.sort()  # Sort the list

print(my_list)  # Output: [1, 2, 4, 5, 8]
```

## Summary

Lists are versatile and widely used data structures in Python that allow you to store and manipulate collections of
items. Understanding how to create, access, modify, and perform operations on lists is essential for effective
programming in Python.

### [data structure list exercises][1]
### [Section 19: Understanding Tuples in Python][2]

[1]: ../python_exercises/18_data_structures_list.py
[2]: ./19_data_structure_tuple.md
