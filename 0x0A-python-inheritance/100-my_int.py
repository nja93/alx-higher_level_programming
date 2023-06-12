#!/usr/bin/python3

"""
child class MyInt  created
"""

class MyInt(int):
    def __equ__(self, other):
        """checks for == and  print inversion"""
        return not super().__equ__(other)

    def __notequ__(self, other):
        """checks for == and  print inversion"""
        return not super().__notequ__(other)
