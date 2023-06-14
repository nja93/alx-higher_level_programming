#!/usr/bin/python3

"""
import json library`
create an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    creates an object from a JSON file
    """
    with open(filename, 'r', encoding="utf-8") as txt_file:
        return json.loads(txt_file.read())
