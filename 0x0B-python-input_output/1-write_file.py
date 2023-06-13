#!/usr/bin/python3

"""
Writes a string to a text file
"""


def write_file(filename="", text=""):

    """Writes a string to a text fil"""
    with open(filename, 'w', encoding="utf-8") as txtfile:
        return txtfile.write(text)
