# Section 1: Comments in Python

Comments are essential in any programming language as they help explain the code and make it more readable. In Python,
you can add comments to your code to provide explanations or notes to yourself and other developers. Comments are
ignored by the Python interpreter and are meant solely for human readers.

## Single-line Comments

To add a single-line comment in Python, use the `#` symbol. Anything following the `#` on the same line will be treated
as a comment and will not be executed. For example:

```python
# This is a single-line comment
name = "John"  # This is also a comment
```

## Multi-line Comments

Python does not have a built-in syntax for multi-line comments like some other programming languages. However, you can
use triple-quotes (either single or double) to create multi-line strings, which are used as documentation strings a.k.a.
docstrings.
PEP 257 describes good docstring conventions. Note that most importantly, the """ that ends a multiline docstring should
be on a line by itself:

```python
"""This is a multi-line comment.
You can add as many lines as you need.

It's enclosed in triple-quotes.
"""
```

For one liner docstrings, please keep the closing """ on the same line:

```python
"""This is a documentation"""
```

While the above method works for multi-line comments, it's more common to use single-line comments for brief
explanations and docstrings (multi-line strings) for more extensive comments and documentation.

Commenting Best Practices
Here are some best practices for using comments in your Python code:

* Use comments to explain complex code, provide context, or document your code's purpose.
* Keep comments concise and to the point. Avoid overly long comments that are hard to read.
* Avoid redundant comments that simply repeat what the code does. Focus on explaining why something is done, not what is
  done.
* Update comments when you modify code to ensure they remain accurate and helpful.
* Use clear and meaningful variable and function names to reduce the need for excessive comments.

Remember that well-written code with meaningful variable and function names can often make your code more
self-explanatory, reducing the reliance on comments.



### [Comments exercises][1]
### [Section 2: Variables in Python][2]


[1]: ../python_exercises/01_comments.py
[2]: ./02_variables.md