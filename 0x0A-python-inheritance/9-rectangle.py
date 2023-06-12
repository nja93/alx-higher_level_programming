#!/usr/bin/python3

"""Defines a subclass Rectangle that inherits from Parent class BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rep a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle subclass.

        Args:
            width type(int): width of the new Rectangle
            height type(int): height of the new Rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Compute the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print the print() and str() representation of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
