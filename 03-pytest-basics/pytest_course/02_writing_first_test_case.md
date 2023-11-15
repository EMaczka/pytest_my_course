# Section 2: Writing the First Test

In this section, we'll create a simple test using Pytest to demonstrate how to write a basic test case. Pytest follows a
convention that makes it easy to get started with writing tests.

## Test Function Structure

A basic test in Pytest is a Python function that starts with "test_". Pytest identifies these functions as test cases
and runs them automatically.

## Creating a Test

Create a Python File:

Start by creating a Python file, for example, `test_example.py`. This file will contain the test functions.

Write a Test Function:

Inside `test_example.py`, write a simple test function. For example:

```python
def test_addition():
    result = 2 + 3
    assert result == 5  # This line is checking the statement
```

Here, we're testing the addition of 2 and 3, expecting the result to be 5.

## Running the Test

Open a Terminal/Command Prompt:

Navigate to the directory where `test_example.py` is located.

Run the Test using Pytest:

Execute the following command to run the test using Pytest:

```bash
pytest test_example.py
```

Pytest will automatically discover and run the test functions in the specified file.

View the Results:

You should see output indicating the test was run and whether it passed or failed. For the simple addition test, it
should pass.

```plaintext
Copy code
============================= test session starts =============================
...
collected 1 item

test_example.py .                                                      [100%]

========================== 1 passed in 0.01 seconds ===========================
```

The `.` indicates that one test passed.

## Understanding the Test

In the test function, we use the `assert` statement to verify if the result of the addition is equal to 5. If it is, the
test passes. If not, the test fails, and Pytest will provide details about the failure.

## Writing More Tests

You can add more test functions to `test_example.py` following the same naming convention, starting with "test_".

Now you have successfully written and run your first test using Pytest.

## Next task

### [Exercise 1: First Pytest exercises][1]
### [Section 3: Structure of a Pytest Test][2]


[1]: ../pytest_exercises/01_first_application_test.md
[2]: 03_pytest_structure.md