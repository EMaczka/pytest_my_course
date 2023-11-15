# Pytest basics

## Objectives

Understanding of basic pytest features and getting familiar with pytest framework

## Pytest: An Overview

Pytest is a powerful and widely used testing framework for Python. It allows efficient and straightforward unit testing.
Some of its key features include:

* **Simplicity and Readability:** Pytest tests are concise and easy to write due to its simple and intuitive syntax.
* **Automatic Test Discovery:** Pytest automatically discovers and runs all files named `test_*.py` or `*_test.py` in
  the project directory.
* **Fixture Management:** Provides robust support for setup, teardown, and dependencies using fixtures.
* **Rich Ecosystem:** Offers a vast array of plugins and integrations for extended functionality.
* **Powerful Assertions:** Allows the use of built-in or custom assertions for effective result validation.

## Why Choose Pytest?

* **Simplicity and Readability:** Pytest tests are easy to read and write, even for beginners.
* **Minimal Boilerplate Code:** Requires less code to achieve the same functionality compared to other testing
  frameworks.
* **Powerful and Extensible:** Can be extended through plugins and easily integrated with other tools and libraries.
* **Great Documentation and Community Support:** Pytest has well-documented features and an active community, making it
  easy to find solutions and get help.

In this section, we will delve into how to set up and use Pytest for effective software testing, covering various
features and best practices.

# Pytest sources

* [Section 1: Installing Pytest][1]
* [Section 2: Writing the First Test][2]
* [Section 3: Structure of a Pytest Test][3]
* [Section 4: Assertions in Pytest][4]
* [Section 5: Fixtures in Pytest][5]
* [Section 6: Fixture parametrize][6]
* [Section 7: Skipping Tests in Pytest][7]
* [Section 8: conftest in Pytest][8]
* [Section 9: Understanding pytest.ini][9]
* [Section 10: Why Use an Empty `__init__.py` File in Pytest?][10]

# Next task
**[Pytest-xdist][next]**

[1]: pytest_course/01_installing_pytest.md
[2]: pytest_course/02_writing_first_test_case.md
[3]: pytest_course/03_pytest_structure.md
[4]: pytest_course/04_assertions.md
[5]: pytest_course/05_fixtures.md
[6]: pytest_course/06_fixture_parametrize.md
[7]: pytest_course/07_skipping_tests.md
[8]: pytest_course/08_conftest.md
[9]: pytest_course/09_pytest_ini.md
[10]: pytest_course/10_init_file.md
[next]: ../04-pytest-xdist/README.md
