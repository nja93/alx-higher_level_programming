#!/usr/bin/python3

"""Defines a subclass Rectangle."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rep a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle subclass.

        Args:
            width (int): width of the new Rectangle
            height(int): height of the new Rectangle
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
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
