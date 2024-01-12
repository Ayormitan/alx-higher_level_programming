#!/usr/bin/python3
"""Function check if the object is an instance of a class """
def inherits_from(obj, a_class):
    """ if the object is an instance of a class 
        Args:
            obj: Object checked
            a_class: class checked for
        Return:
            Always true when obj is an instance else return false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
