#!/usr/bin/python3
"""Define class Square"""
class Square:
    """Initialize attributes for the claas"""
    def __init__(self, size=0):
        """Check for instances and return Errors"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
