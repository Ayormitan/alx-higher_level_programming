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
        self._width = width
        self._height = height
    @property
    def width(self):
        """ Width getter"""
        return self._width
    @property
    def height(self):
        """heigth getter"""
        return self._height
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._heigth = value
    def area(self):
        """ area of the rectangle"""
        return self.width * self.height
    def perimeter(self):
        """"perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + self.height
