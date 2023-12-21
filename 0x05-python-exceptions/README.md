# 0x05. Python - Exceptions

## Requirements

### General
- **Allowed Editors**: vi, vim, emacs
- **OS**: Ubuntu 20.04 LTS
- **Python Version**: 3.8.5
- **File Endings**: All files should end with a new line.
- **Shebang**: The first line of all files should be `#!/usr/bin/python3`.
- **README.md**: A mandatory README.md file should be present at the project root.
- **Code Style**: Use `pycodestyle` (version 2.8.*).
- **File Permissions**: All files must be executable.
- **File Length**: The length of your files will be tested using `wc`.

## Tasks

### Task 0: Print Elements of a List

- **Prototype**: `def safe_print_list(my_list=[], x=0):`
- **Description**: Write a function to print `x` elements of a list. Use `try`/`except` for error handling. Restrictions apply on the usage of modules and built-in functions.

### Task 2: Print an Integer

- **Prototype**: `def safe_print_integer(value):`
- **Description**: Write a function to print an integer using the `"{:d}".format()` method. Return `True` if the value is printed correctly, otherwise `False`.

### Task 3: Print Integers from a List

- **Prototype**: `def safe_print_list_integers(my_list=[], x=0):`
- **Description**: Write a function to print the first `x` integers from a list. Only integers should be printed, other types should be ignored.

### Task 3 (Duplicate): Divide 2 Integers

- **Prototype**: `def safe_print_division(a, b):`
- **Description**: Write a function to divide two integers and print the result using `try`/`except`/`finally`.

### Task 4: Divide Element by Element

- **Prototype**: `def list_division(my_list_1, my_list_2, list_length):`
- **Description**: Write a function to divide elements of two lists element-wise. Handle various error conditions and return a new list.

### Task 5: Raise a Type Exception

- **Prototype**: `def raise_exception():`
- **Description**: Write a function that raises a type exception without importing any modules.

### Task 6: Raise a Name Exception with Message

- **Prototype**: `def raise_exception_msg(message=""):`
- **Description**: Write a function that raises a name exception with a custom message without importing any modules.

