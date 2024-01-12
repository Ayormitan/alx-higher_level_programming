#!/usr/bin/python3
""" A class defination for BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """A rectangle using base geomtry fron 7-base_geometry"""
    def __init__(self, width, height):
        """ Initializes a new rectangle
        Args:
            Width (int): The width of the rectangle
            height (int): The height of the new triangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", width)
        self.__height = height
