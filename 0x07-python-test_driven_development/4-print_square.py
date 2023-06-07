#!/usr/bin/python3
"""
Defines a function that prints a square

"""


def print_square(size):
    """
    Prints a square with #

    Raises:
        TypeError: If size is not of integer data type
        TypeError: If size is a float and less than 0
        ValueError: If size is less than 0

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print("")

