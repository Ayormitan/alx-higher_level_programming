#!/usr/bin/python3
"""A class defined in base"""
class Base:
    """
    private class attribute
    """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """ initializes attribute"""
        if id is not None:
            self.id = id  # assign id if provided
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects 
