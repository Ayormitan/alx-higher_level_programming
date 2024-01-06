#!/usr/bin/python3
"""class defination for rectangle"""

class Rectangle:
    """represents a rectanglee"""
    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle

        Args:
            width
            height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """heigth getter"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """"perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
