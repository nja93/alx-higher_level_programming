#!/usr/bin/python3
def to_uper(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return chr(ord(c) - 32)
    else:
        return ord(c)


def uppercase(string):
    new_str = ""
    for c in string:
        new_str += "%c" % to_uper(c)
    print("{:s}".format(new_str))

