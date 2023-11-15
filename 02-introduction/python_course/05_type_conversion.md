# Section 5: Type Conversion in Python

Type conversion, also known as type casting, is the process of changing the data type of a variable from one type to
another. Python provides several built-in functions for performing type conversion. Let's explore type conversion in
more detail:

## Implicit Type Conversion (Auto Type Conversion)

Python automatically performs type conversion when it makes sense and won't result in a loss of data. This is often
referred to as implicit type conversion. For example:

```python
x = 5  # 'x' is an integer
y = 3.14  # 'y' is a floating-point number
```

result = x + y # 'result' is a floating-point number (implicit conversion)
In the above code, Python automatically converts the integer x to a floating-point number to perform the addition.

## Explicit Type Conversion (Type Casting)

Explicit type conversion, also known as type casting, is when you manually change the data type of a variable using
functions provided by Python. Here are some commonly used type conversion functions:

* int(): Converts a value to an integer.
* float(): Converts a value to a floating-point number.
* str(): Converts a value to a string.

For example:

```python
num_str = "42"  # 'num_str' is a string
num_int = int(num_str)  # Convert 'num_str' to an integer

pi = 3.14  # 'pi' is a floating-point number
pi_str = str(pi)  # Convert 'pi' to a string
```

## Handling Errors

It's important to note that type conversion may result in errors if the conversion is not possible. For example,
converting a non-numeric string to an integer will raise a ValueError. To avoid errors, you should ensure that the data
you're converting is compatible with the target type.

```python
num_str = "abc"
# The following line will raise a ValueError
num_int = int(num_str)
```

## Sumary

Type conversion allows you to work with different data types and perform operations that require compatible types.
Understanding when and how to perform type conversion is a valuable skill in Python programming.

### [type conversion exercises][1]
### [Section 6: Comparison Operators in Python][2]


[1]: ../python_exercises/05_type_conversion.py
[2]: ./06_comparision_operators.md