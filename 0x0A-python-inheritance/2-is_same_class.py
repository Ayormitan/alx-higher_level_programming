#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.
            
    Args:
    - obj: An object to check.
    - cls: A class or tuple of classes to compare against.
                            
    Returns:
     - True if obj is exactly an instance of cls; otherwise, False.
    """
    if (type(obj)) == a_class:
        return True
    return False
