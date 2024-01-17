. Python - Almost a circle Resources

## Table of Contents
- [args/kwargs](#argskwargs)
- [JSON encoder and decoder](#json-encoder-and-decoder)
- [unittest module](#unittest-module)
- [Python test cheatsheet](#python-test-cheatsheet)

# Task 1: Create a file named tests

Create a file named `tests`.

# Task 2: Write the first class Base:

Create a folder named `models` with an empty file `__init__.py` inside - with this file, the folder will become a Python package.

Create a file named `models/base.py`:

## Class Base:

- Private class attribute `__nb_objects = 0`
- Class constructor: `def __init__(self, id=None):`
  - If `id` is not `None`, assign the public instance attribute `id` with this argument value. You can assume `id` is an integer, and you dont need to test the type of it.
  - Otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`.

This class will be the base of all other classes in this project. The goal of it is to manage the `id` attribute in all your future classes and to avoid duplicating the same code (by extension, the same bugs).


**Author:** Ayomitan Omotayo
