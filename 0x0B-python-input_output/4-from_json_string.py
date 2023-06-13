#!/usr/bin/python3

"""
import JSON data structures
"""

import json


def from_json_string(my_str):
    """
    returns a python object rep by a JSON string
    """
    return json.loads(my_str)
