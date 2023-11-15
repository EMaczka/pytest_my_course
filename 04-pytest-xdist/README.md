# Pytest-xdist

## Installation
First, you need to install the pytest-xdist plugin. You can do this using pip:

```bash
pip install pytest-xdist
```

## Running Tests in Parallel
Once `pytest-xdist` is installed, you can use its options to run tests in parallel.

## Running Tests Across Multiple CPUs
The most straightforward way to leverage parallel execution is to use the `-n` option, specifying the number of CPUs you want to use:

```bash
pytest -n <num_cpus>
```
For example, to run tests across 2 CPUs:

```bash
pytest -n 2
```

## Run specific test file
To run a specific test file using `pytest-xdist`, you can use the `-k` option (similar to standard Pytest) and simultaneously use the `-n` option for parallel execution. Here's an example:

```bash
pytest -k <test_or_marker_name> -n <num_cpus> path/to/test_file.py
```

Replace `<test_or_marker_name>` with the specific test name or marker, and `path/to/test_file.py` with the path to the test file you want to run in parallel.

For example, if you have a file named `test_example.py` and you want to run tests with the smoke marker in parallel on two CPUs, the command could look like this:

```bash
pytest -k smoke -n 2 tests/test_example.py
```
Keep in mind that parallel test execution has its limitations and requires tests to be independent of each other. Ensure that your tests are properly written to handle parallel execution, and check for any resource conflicts between tests.