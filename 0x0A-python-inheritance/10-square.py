#!/usr/bin/python3

"""
create class Square, subclass of module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A subclass of Rectangle
    Args:
        def __init__(self, size) - Constructor
    """
    def __init__(self, size):
        """initialize private attribute size, and then validates it"""
        self.integer_validator("size", size)  
        self.__size = size

    def area(self):
        """returns area of  square"""
        return self.__size ** 2
    def __str__(self):
        """Print in readable format"""
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)
