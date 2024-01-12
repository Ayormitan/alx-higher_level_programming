#!/usr/bin/python3
"""Defines a class geometry"""
class BaseGeometry:
    """ Privates instances method
    """
    def area(self):
        """Raises an exemption of not implemented"""
        raise Exception("area() is not implemented")
