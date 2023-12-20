# 0x06. Python - Classes and Objects

## Requirements

### General
- **Allowed editors:** vi, vim, emacs
- **OS:** Ubuntu 20.04 LTS
- **Python version:** 3.8.5
- **File requirements:**
  - All files must end with a new line.
  - The first line of all your files should be `#!/usr/bin/python3`.
  - Your code should use pycodestyle (version 2.8.*).
  - All files must be executable.
  - Length of files will be tested using wc.
- **Documentation requirements:**
  - Modules, classes, and functions must have documentation explaining their purpose.

### Tasks

1. **Empty Square Class**
    - Write an empty class `Square` that defines a square without importing any module.

2. **Square Class with Size**
    - Private instance attribute: `size`.
    - Instantiation with size without type/value verification.

3. **Square Class with Size Verification**
    - Private instance attribute: `size`.
    - Instantiation with optional size: 
        - `def __init__(self, size=0):`
    - Error handling:
        - Raise `TypeError` if size is not an integer.
        - Raise `ValueError` if size is less than 0.

4. **Square Class with Area Method**
    - Private instance attribute: `size`.
    - Instantiation with optional size.
    - Public instance method: `def area(self):` returns the current square area.

5. **Square Class with Size Properties**
    - Private instance attribute: `size`.
    - Property to retrieve size and setter to set it.
    - Instantiation with optional size.
    - Public instance method: `def area(self):` returns the current square area.

6. **Square Class with Printing Method**
    - Private instance attribute: `size`.
    - Property to retrieve size and setter to set it.
    - Instantiation with optional size.
    - Public instance methods:
        - `def area(self):` returns the current square area.
        - `def my_print(self):` prints the square using `#` characters.

7. **Square Class with Position**
    - Private instance attributes: `size` and `position`.
    - Properties to retrieve size and position and setters to set them.
    - Instantiation with optional size and optional position.
    - Public instance methods:
        - `def area(self):` returns the current square area.
        - `def my_print(self):` prints the square using `#` characters with specified position.


