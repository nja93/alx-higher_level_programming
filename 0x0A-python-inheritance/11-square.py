#!/usr/bin/python3
"""
Create a subclass Square, child class of Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square Created

    Args:
        def __init__(self, size) - is the  Constructor
    """
    def __init__(self, size):
        """
        Constructor initialized
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        calculate area
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
        Print in readable format
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
