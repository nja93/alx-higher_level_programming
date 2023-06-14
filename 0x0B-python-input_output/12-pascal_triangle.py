#!/usr/bin/python3

"""
method that returns a list of int rep Pascal's Triangle or 
empty list if n <= 0
"""


def pascal_triangle(n):
    """
    initialize triangle with 1st List [1].
    iterate from index position 1 to i-1 as
    the first and last elemrnt aere excluded
    You can assume n will be always an integer
    """
    triangle_p = []
    if n <= 0:
        return tri
    if n == 0:
        return [[1]]
    triangle_p = [[1]]
    for i in range(n-1):
        tri.append([a+b for a, b in zip([0] + triangle_p[-1], triangle_p[-1] + [0])])
    return triangle_p
