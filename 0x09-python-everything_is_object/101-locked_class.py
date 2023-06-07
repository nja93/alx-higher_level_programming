#!/usr/bin/python3
"""defines a locked class"""


class LockedClass:
    """ 
    limits the user  only createthe new instance attribute is called "first_name"
    """

    __slots__ = ["first_name"]
