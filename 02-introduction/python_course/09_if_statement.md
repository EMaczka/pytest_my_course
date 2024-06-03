# Section 9: The "if" Statement in Python

The "if" statement in Python is a fundamental control structure that allows you to make decisions in your code. It
enables your program to execute different blocks of code based on whether a specified condition is true or false. Let's
explore how the "if" statement works:

## Basic "if" Statement

The basic syntax of the "if" statement is as follows:

```python
if condition:
# Code to execute if the condition is True
```    

Here's an example using an "if" statement:

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

In this example, the code block inside the "if" statement will be executed because the condition `x > 5` is true.

## "if-else" Statement

The "if-else" statement allows you to specify an alternative code block to execute if the condition is false. Here's the
syntax:

```python
if condition:
# Code to execute if the condition is True
else:
# Code to execute if the condition is False
```

Example:

```python
x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

In this case, the "else" block will be executed because the condition `x > 5` is false.

## "if-elif-else" Statement

The "if-elif-else" statement allows you to handle multiple conditions sequentially. You can have multiple "elif" (short
for "else if") blocks in addition to the "if" and "else" blocks. Here's the syntax:

```python
if condition1:
# Code to execute if condition1 is True
elif condition2:
# Code to execute if condition2 is True
else:
# Code to execute if none of the conditions are True
```

Example:

```python
x = 3

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

In this example, the "elif" block with `x == 5` will be executed because none of the previous conditions are true.

## Summary

The "if" statement is a fundamental building block of Python programming that allows you to create conditional logic in
your code. It enables you to make decisions and execute specific code blocks based on the evaluation of conditions.
Understanding how to use "if" statements is essential for writing dynamic and responsive programs.

### [if statement exercises][1]
### [Section 10: The "while" Loop in Python][2]


[1]: ../python_exercises/09_if_statement.py
[2]: ./10_while_loop.md