# Section 1: Installing Pytest

---
### Important
**Instruction of installing pytest for pycharm is below this section**

---

Before you can start using Pytest for writing and running tests, you need to install it. Pytest can be easily installed
using Python's package manager, pip.

## Prerequisites

* Python: Ensure you have Python installed on your system. Pytest is compatible with Python 2.7, 3.5+, and PyPy.

## Installing Pytest using pip

**Open a Terminal/Command Prompt:**

* On Windows, you can open the Command Prompt by searching for "cmd" in the Start menu.
* On macOS or Linux, you can use the Terminal application.

**Use pip to install Pytest:**

Run the following command to install Pytest and its dependencies:

```bash
pip install pytest
```

If you have multiple Python versions installed or need to install it for a specific version, you can use pip3 for Python
3.x:

```bash
pip3 install pytest
```

This will download and install the latest version of Pytest from the Python Package Index (PyPI).

**Verify the Installation:**

To confirm that Pytest has been installed correctly, run:

```bash
pytest --version
```

This command should display the Pytest version that was installed.

## Upgrading Pytest

To upgrade Pytest to the latest version, you can use pip to install the latest release:

```bash
pip install --upgrade pytest
```

## Verifying the Installation in a Python Script

You can create a simple Python script to test if Pytest is correctly installed:

Create a file named `test_hello.py` with the following content:

```python
def test_hello():
    assert "hello" == "hello"
```

Run the test using Pytest:

```bash
pytest test_hello.py
```

If everything is set up correctly, you should see output indicating that one test was run and passed.

Now you have Pytest successfully installed and ready to use for writing and running tests.

---

# Installing Pytest in PyCharm
PyCharm is a popular integrated development environment (IDE) for Python that supports managing Python packages and testing frameworks. Here's how you can install Pytest in PyCharm:

1. **Open PyCharm:**
   * Launch the PyCharm IDE on your computer.

2. **Create a New Project or Open an Existing Project:**
   * Create a new Python project or open an existing one in which you want to install and use Pytest.

3. **Open the Terminal:**
   * Once you have your project open, navigate to the terminal within PyCharm. You can find the terminal tab usually at the bottom of the PyCharm window.

4. **Install Pytest using pip:**
   * In the terminal, run the following command to install Pytest using pip:
```bash
pip install pytest
```

If you're using Python 3, you can use `pip3` instead:

```bash
pip3 install pytest
```
PyCharm will display the installation progress and notify you once it's completed.

5. **Verify the Installation:**
To confirm that Pytest is installed, you can run the following command in the terminal:

```bash
pytest --version
```
This should display the version of Pytest that was installed.

6. **Creating a Pytest Configuration:**

PyCharm allows you to create a run configuration for Pytest to make running tests within the IDE more convenient. To create a Pytest configuration, follow these steps:

* Click on the "Edit Configurations" dropdown in the top right corner.
* Click on the `+` icon to add a new configuration and choose "Python tests" -> "pytest".
* Configure the options as needed, specifying the directory where your tests are located.
* Save the configuration.

Now you have Pytest installed in your PyCharm project, and you can easily run your tests from within the IDE.

## Next task
### [Section 2: Writing the First Test][1]

[1]: 02_writing_first_test_case.md

