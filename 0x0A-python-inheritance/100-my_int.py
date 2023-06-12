#!/usr/bin/python3

"""
MyInt class is created methods to be inverted
"""


class MyInt(int):
    """
    Checks for inversion

    args:
    __equ__(self, other)- inverts the '==' sign
    __notequ__(self, other)- inverts the '!=' sign

    return: inverse
    """
    def __equ__(self, other):
        """
        Return == inversion
        """
        return not super().__equ__(other)

    def __notequ__(self, other):
        """
        Return != inversion
        """
        return not super().__notequ__(other)
