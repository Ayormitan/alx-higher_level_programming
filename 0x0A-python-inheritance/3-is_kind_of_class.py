#!/usr/bin/python3
""" Function defines class and instance"""
def is_kind_of_class(obj, a_class):
    """ Function will check for type of class using isinstance
    Args:
        obj (any): Object to check
        a_class (type): class type
    Returns:
            true If object is an instance or it is inherited else false
    """
    if isinstance (obj, a_class):
        return True
    return False
