# Section 3: Structure of a Pytest Test

Pytest provides a flexible and intuitive way to structure your tests, making it easy to organize and manage your test
suite efficiently.

## Test Functions

In Pytest, a test is represented by a Python function that starts with "test_". These functions encapsulate individual
test cases.

Example of a simple test function:

```python
def test_addition():
    result = 2 + 3
    assert result == 5
```

## Folder and File Structure
When organizing tests, it's important to maintain a clear and understandable folder and file structure to facilitate test management and easy access. Here's a typical structure:

```lua
project_root/
|-- tests/
|   |-- test_math.py
|   |-- test_strings.py
|   |-- ...
|-- src/
|   |-- my_module.py
|   |-- ...
|-- requirements.txt
|-- ...
```
Structure Overview:
* **project_root/:** The main project folder.

* **tests/:** The folder where you store test-related files.
  * **test_math.py:** File containing tests related to mathematical functions.
  * **test_strings.py:** File containing tests related to string manipulation.
* **src/:** The folder where you store the project's source code.
  * **my_module.py:** File containing the code for a module with functions to be tested.
* **requirements.txt:** File containing a list of dependencies and versions for your project.

## Grouping Tests with Classes
By using classes, we can add an additional level of grouping to our tests. For example:

* **test_math.py:**

```python
class TestMathFunctions:
    def test_addition(self):
        assert 2 + 3 == 5

    def test_subtraction(self):
        assert 5 - 3 == 2
```
* **test_strings.py:**

```python
class TestStringManipulation:
    def test_concatenation(self):
        result = "Hello, " + "world!"
        assert result == "Hello, world!"

    def test_uppercase(self):
        result = "hello".upper()
        assert result == "HELLO"
```

Now we have tests related to mathematics and string manipulation grouped into separate classes.

## Running Specific Tests

Pytest allows you to run specific tests, classes, or modules:

Run Specific Test Function:

```bash
pytest test_example.py::test_addition
```

Run Specific Test Class:

```bash
pytest test_example.py::TestMathFunctions
```

Run All Tests in a Module:

```bash
pytest test_example.py
```

## Next task
### [Section 4: Assertions in Pytest][1]

[1]: 04_assertions.md
