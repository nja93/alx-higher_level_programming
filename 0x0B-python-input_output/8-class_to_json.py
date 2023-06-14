#!/usr/bin/python3
"""
return dictionary desc for JSON serialization of an object
Class to JSON
"""


def class_to_json(obj):
    """
    returns dictionary desc for JSON serialization of an object
    can also be written as return obj.__dict__
    """
    return vars(obj)
