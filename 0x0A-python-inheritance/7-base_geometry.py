#!/usr/bin/python3
"""
Creates a BaseGeometry class
"""


class BaseGeometry:
    """Class with methods"""

    def area(self):
        """Raises an Exception with the message:
        area() is not implemented
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Checks if value id of type int and greater than or equal to 0"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
