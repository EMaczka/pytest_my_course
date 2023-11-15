# Section 9: Understanding pytest.ini
Location
The `pytest.ini` file should be located in the root directory of your project or in any of its parent directories.

```lua
project_root/
|-- pytest.ini
|-- tests/
|   |-- test_file1.py
|   |-- test_file2.py
|-- src/
|   |-- your_module.py
|-- ...
```

Basic Structure
Here's a basic structure of a pytest.ini file:

```plaintext
[pytest]
option=value
```
The [pytest] section contains various configuration options in the form of option=value.

Common Configuration Options
addopts:

This option allows you to pass additional command-line options to Pytest.

```plaintext
[pytest]
addopts = -v --html=report.html
```
markers:

Define custom markers that can be used in tests.

```plaintext
[pytest]
markers =
    smoke: Mark a test as a smoke test.
    regression: Mark a test as a regression test.
```
You can then use these markers in your tests:

```python
import pytest

@pytest.mark.smoke
def test_smoke_test():
    assert True

@pytest.mark.regression
def test_regression_test():
    assert True
```
norecursedirs:

Exclude specific directories from being searched for tests.

```plaintext
[pytest]
norecursedirs = .* build dist CVS _darcs {arch} *.egg venv
```
python_files:

Match files with specific patterns to be considered as test files.

```plaintext
[pytest]
python_files = test_*.py *_test.py
```
filterwarnings:

Filter specific warnings, displaying them as errors or ignoring them.

```plaintext
[pytest]
filterwarnings =
    error
    ignore:.*is deprecated.*
```
log_cli:

Control log output to the console during test runs.

```plaintext
[pytest]
log_cli = true
```
log_cli_level:
Set the log level for console output. Options include DEBUG, INFO, WARNING, ERROR, and CRITICAL.

```plaintext
[pytest]
log_cli_level = INFO
```
Example Usage
```plaintext
[pytest]
addopts = -v --html=report.html
markers =
    smoke: Mark a test as a smoke test.
    regression: Mark a test as a regression test.
python_files = test_*.py
filterwarnings =
    error
    ignore:.*is deprecated.*
```
In this example, we've configured additional command-line options, defined custom markers, specified test file patterns, and set warning filtering.

The `pytest.ini` file provides a way to configure and customize various aspects of Pytest for your project, making it easier to manage and run your tests according to your requirements.

## Next task
### [Exercise 7: using pytest.ini file][1]
### [Section 10: Why Use an Empty `__init__.py` File in Pytest?][2]

[1]: ../pytest_exercises/07_pytest_ini.md
[2]: 10_init_file.md
