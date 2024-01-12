#!/usr/bin/ptyhon3
""" Function defines class and instance"""
def is_kind_of_class(obj, a_class):
    """ 
    Function will check for type of class using isinstance
    args:
        obj: Object to check
        a_class: class type
    """
    if isinstance(obj, a_class):
        return True
    return False
