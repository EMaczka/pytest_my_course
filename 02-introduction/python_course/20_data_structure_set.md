# Section 20: Understanding Sets in Python

Sets are a fundamental data structure in Python used to store a collection of unique elements. Sets are unordered and
mutable, meaning you can modify the elements in a set, but they don't have a specific order. Additionally, sets do not
allow duplicate elements. Let's explore how sets work and how to use them effectively:

## Creating a Set

A set is created by enclosing elements within curly braces `{}`, separated by commas.

### Example

```python
my_set = {1, 2, 3, 4}
```

In this example, my_set is a set containing four unique elements.

## Set Operations

Sets support various operations like adding elements (`add()`), removing elements (`remove()`), checking
membership (`in`), and finding the length (`len()`).

```python
my_set = {1, 2, 3}

my_set.add(4)  # Add an element
my_set.remove(2)  # Remove an element
set_length = len(my_set)  # Get the length of the set
element_in_set = 3 in my_set  # Check if an element is in the set

print(my_set)  # Output: {1, 3, 4}
print(set_length)  # Output: 3
print(element_in_set)  # Output: True
```

## Set Methods

Sets have built-in methods for various operations, including union (`union()`), intersection (`intersection()`),
difference (`difference()`), and more.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)  # Union of sets
intersection_set = set1.intersection(set2)  # Intersection of sets
difference_set = set1.difference(set2)  # Difference of sets

print(union_set)  # Output: {1, 2, 3, 4, 5}
print(intersection_set)  # Output: {3}
print(difference_set)  # Output: {1, 2}
```

## Frozen Sets

In addition to regular sets, Python also has "frozen sets" (`frozenset`), which are immutable and can be used as
elements in other sets.

```python
fs = frozenset([1, 2, 3])

my_set = {fs, 4, 5}

print(my_set)  # Output: {frozenset({1, 2, 3}), 4, 5}
```

## Summary

Sets are useful data structures in Python for storing unique elements. They are particularly handy when you need to
perform set operations like union, intersection, and difference. Understanding how to create, modify, and use sets
effectively is important for various programming tasks in Python.

### [data structure sets exercises][1]
### [Section 21: Understanding Dictionaries in Python][2]

[1]: ../python_exercises/20_data_structures_set.py
[2]: ./21_data_structure_dictionary.md
