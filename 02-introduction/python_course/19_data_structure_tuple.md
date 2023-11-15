# Section 19: Understanding Tuples in Python

Tuples are a fundamental data structure in Python used to store collections of items, similar to lists. However, tuples
are immutable, meaning their elements cannot be modified once created. Tuples are commonly used to group related data
together. Let's explore how tuples work and how to use them effectively:

## Creating a Tuple

A tuple is created by enclosing elements within parentheses `()`, separated by commas.

```python
my_tuple = (1, "hello", 3.14, True)
```

In this example, my_tuple is a tuple containing four elements of different data types.

## Accessing Elements

Elements in a tuple are accessed by their index, starting from 0 for the first element.

```python
my_tuple = (10, 20, 30, 40)

print(my_tuple[0])  # Output: 10
print(my_tuple[2])  # Output: 30
```

## Immutable Nature

Tuples are immutable, meaning their elements cannot be modified once the tuple is created.

```python
my_tuple = (10, 20, 30)

# Attempting to modify an element (will result in an error)
# my_tuple[1] = 25
```

The above example will raise a `TypeError` since tuples do not support item assignment.

## Tuple Operations

Tuples support operations like concatenation (`+`) and repetition (`*`), similar to lists.

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5)

concatenated_tuple = tuple1 + tuple2
repeated_tuple = tuple1 * 3
tuple_length = len(tuple1)

print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5)
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(tuple_length)  # Output: 3
```

## Tuple Methods

Tuples have limited methods due to their immutability. Common methods include `count()` and `index()`.

```python
my_tuple = (1, 2, 2, 3, 3, 3)

count_of_2 = my_tuple.count(2)  # Count occurrences of 2
index_of_3 = my_tuple.index(3)  # Get index of the first 3

print(count_of_2)  # Output: 1
print(index_of_3)  # Output: 3
```

## Summary

Tuples are useful data structures in Python for grouping related data. While they are similar to lists, their
immutability makes them suitable for scenarios where data should not be changed. Understanding how to create, access,
and use tuples effectively is important for writing efficient and maintainable Python code.

### [data structure tuples exercises][1]
### [Section 20: Understanding Sets in Python][2]

[1]: ../python_exercises/19_data_structures_tuple.py
[2]: ./20_data_structure_set.md
