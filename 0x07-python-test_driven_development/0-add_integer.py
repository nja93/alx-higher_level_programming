#!/usr/bin/python3

"""
Addition function that adds 2 integers
"""
def add_integer(a, b=98):
    """
    a & b must be int or float,

    else,

    raise a typeerror message "a must be an integer or b must be an integer"
    then, cast them to int type if float

    return sum"

    """


    """
    check if a and b are either int or float type
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    """
    typecasting them into int type
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
