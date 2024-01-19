#!/usr/bin/python3
""" define a rectangle class"""
from models.base import Base
class Rectangle(Base):
    """represents a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initailizes the rectangle

        Args:
            width (int): Width of rectangle
            height (int): Heigth of the rectanglew
            x (int): X cordinate
            y (int): y cordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width of a rectangle"""
        return self.__width
    @width.setter
    def width(self, value):
        """set the width o the rectangle"""
        self.__width = value
    @property
    def height(self):
        """get the height of a rectangle"""
        return self.__height
    @height.setter
    def height(self, value):
        """get the height of a rectangle""" 
        self.__height = value
    @property
    def x(self):
        """get the height of a rectangle""" 
        return self.__x
    @x.setter
    def x(self, value):
        """get the height of a rectangle""" 
        self.__x = value
    @property
    def y(self):
        """get the height of a rectangle"""
        return self.__y
    @y.setter
    def y(self, value):
        """get the height of a rectangle""" 
        self.__y = value
