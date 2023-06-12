#!/usr/bin/python3

"""
Defines a class-checking function
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an instance belongs to a class
    """
    if isinstance(obj, a_class):
        return True
    return False
