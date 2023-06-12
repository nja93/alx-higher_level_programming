#!/usr/bin/python3

"""Defines is_same_class a class-checking fn"""


def is_same_class(obj, a_class):
    """Check if an object is exactly same type/an instance of a given class.

    Args:
        obj (any): object to check.
        a_class (type): The class to match the type of obj against
    Returns:
        If obj is exactly of type/instance of a_class return True.
    Else - False.
    """
    if type(obj) == a_class:
        return True
    return False
