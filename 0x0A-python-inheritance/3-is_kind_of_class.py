#!/usr/bin/python3

"""
Defines a class-checking function
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance or inherited instance of a class

    Args:
        obj: object to check.
        a_class:  class to match the type of obj to.
    Returns:
        If obj is of type/an instance or inherited instance of a_class return True.
        return - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
