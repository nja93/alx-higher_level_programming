#!/usr/bin/python3

""" Define class Rectangle with width and height as attributes"""

class Rectangle:

    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle

        Args:
            width (int): width of rectangle
            height (int):  height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
         Get/setter for rectangle width
        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get/setter rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
