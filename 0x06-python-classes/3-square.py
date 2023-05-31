#!/usr/bin/python3
"""define a class - Square"""
class Square:
    """
    has a private attribute size
    and checks data type
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size
