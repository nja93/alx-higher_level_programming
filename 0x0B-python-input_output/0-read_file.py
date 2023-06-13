#!/usr/bin/python3

""" Read a text file """


def read_file(filename=""):
    """
    Reads a text file
    """
    with open(filename, encoding="utf-8") as txtfile:
        print(txtfile.read(), end="")
