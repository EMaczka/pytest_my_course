# Section 11: The "for" Loop in Python

The "for" loop is a fundamental control structure in Python used for iterating over sequences like lists, strings,
dictionaries, and more. It allows you to execute a block of code repeatedly for each item in a sequence. Let's explore
how the "for" loop works:

## Basic "for" Loop

The basic syntax of a "for" loop is as follows:

```python
for variable in sequence:
# Code to execute for each item in the sequence
```

Here's an example using a `for` loop to iterate through a list of numbers:

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
```

In this example, the `for` loop iterates through the `numbers` list, and for each iteration, it assigns the value of the
current item to the variable `num`. The code block inside the loop then executes.

## "for" Loop with Range

The `range()` function is often used in combination with `for` loops to generate a sequence of numbers. Here's an
example:

```python
for i in range(5):  # Generates numbers from 0 to 4
    print(i)
```

## "for" Loop with Strings

You can also use a `for` loop to iterate through characters in a string:

```python
text = "Hello"

for char in text:
    print(char)
```

## "for" Loop with Dictionaries

You can use a `for` loop to iterate through keys, values, or key-value pairs in a dictionary:

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

for key in person:
    print(key, person[key])
```

The output will be:

```
nameAlice
age30
cityNew York
```

### or

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

# Iterating through Dictionary Items
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")
```

In this example, we have a dictionary called person, and the for key, value in `person.items()` loop iterates through
key-value pairs in the dictionary. In each iteration, the variable key holds the key, and the variable value holds the
corresponding value. Inside the loop, you can perform operations on the keys and values of the dictionary.

The output of this example will be:

```
Key: name, Value: Alice
Key: age, Value: 30
Key: city, Value: New York
```

## Sumary

The `for` loop is a versatile and powerful tool for iterating through sequences in Python. It simplifies repetitive
tasks and allows you to process data efficiently. Understanding how to use `for` loops is essential for many programming
tasks and can greatly enhance your ability to work with collections of data.

### [for loop exercises][1]
### [Section 12: Functions and Methods in Python][2]


[1]: ../python_exercises/11_for_loop.py
[2]: ./12_functions_and_methods.md

