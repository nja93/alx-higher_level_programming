#!/usr/bin/python3
"""
appends a string to a textfile
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file
    """
    with open(filename, 'a', encoding="utf-8") as txtfile:
        return txtfile.write(text)
