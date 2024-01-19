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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    @property
    def height(self):
        """get the height of a rectangle"""
        return self.__height
    @height.setter
    def height(self, value):
        """get the height of a rectangle""" 
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    @property
    def x(self):
        """get the height of a rectangle""" 
        return self.__x
    @x.setter
    def x(self, value):
        """get the height of a rectangle""" 
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    @property
    def y(self):
        """get the height of a rectangle"""
        return self.__y
    @y.setter
    def y(self, value):
        """get the height of a rectangle""" 
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    def area(self):
        """print the rectangle using #"""
        return self.width * self.height
    def display(self):
        """print rectangle using the '#' char"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range (self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
    def __str__(self):
        """verriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
