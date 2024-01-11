#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
        function will print last name and the first name

        Args:
            first_name: Personal or given name
            last_name: Parents name of individual
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(last_name, first_name))
