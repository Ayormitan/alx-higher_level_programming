#!/usr/bin/ptyhon3
""" Function defines class and instance"""
def is_kind_of_class(obj, a_class):
    """ Function will check for type of class using isinstance
    args:
        obj: Object to check
        a_class: class type
        Returns: True If object is an instance or it is inherited else false
    """
    if isinstance(obj, a_class):
        return True
    return False
