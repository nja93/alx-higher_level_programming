#!/usr/bin/python3

"""importing Rectangle module"""


Rectangle = __import__('9-rectangle').Rectangle

"""Class square that is Rectangle's child"""

class Square(Rectangle):
    """A subclass of Rectangle"""
    def __init__(self, size):
        """initialize private attribute size, and then validates it"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns area of  square"""
        return self.__size ** 2
