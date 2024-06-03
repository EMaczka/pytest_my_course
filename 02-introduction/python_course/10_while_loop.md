# Section 10: The "while" Loop in Python

The "while" loop is a fundamental control structure in Python that allows you to repeatedly execute a block of code as
long as a specified condition is true. It's used for situations where you want to continue executing code until a
certain condition is no longer met. Let's explore how the "while" loop works:

## Basic "while" Loop

The basic syntax of a "while" loop is as follows:

```python
while condition:
# Code to execute as long as the condition is True
```

Here's an example using a "while" loop to count from 1 to 5:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

In this example, the "while" loop continues to execute as long as the condition `count <= 5` is true. The code block
inside the loop increments the `count` variable in each iteration.

## Infinite Loops

Be cautious when using "while" loops, as they can potentially create infinite loops if the condition never becomes
false. It's essential to include a mechanism that can change the condition to false eventually.

```python
# This creates an infinite loop
while True:
    print("This is an infinite loop!")

# To break out of an infinite loop, you can use the "break" statement.
```

## "while" Loop with User Input

You can use a "while" loop to repeatedly prompt the user for input until a specific condition is met:

```python
while True:
    user_input = input("Enter 'q' to quit: ")
    if user_input == 'q':
        break
```

In this example, the "while" loop continues until the user enters 'q', at which point the break statement is used to
exit the loop.

## Summary

The "while" loop is a powerful tool for creating loops in Python that execute as long as a condition remains true. It's
commonly used for tasks that require repeated execution until a certain condition is met. However, you should be
cautious when using "while" loops to avoid creating infinite loops unintentionally.

### [while loop exercises][1]
### [Section 11: The "for" Loop in Python][2]


[1]: ../python_exercises/10_while_loop.py
[2]: ./11_for_loop.md
