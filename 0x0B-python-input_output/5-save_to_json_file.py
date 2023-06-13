#!/usr/bin/python3

"""
import jsonwrite a json string to a .txt file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes a json string to a text file
    """
    with open(filename, 'w', encoding="utf-8") as txt_file:
        txt_file.write(json.dumps(my_obj))
