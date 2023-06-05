#!/usr/bin/python3
"""
    function that returns a new matrix, after div
"""
def matrix_divided(matrix, div):
    """
    Args:
        matrix: list if lists of int/float type
        div: denominator

    Raises:
        TypeError: if matrix elements are not numbers
        TypeError: if matrix contains rows of non equal size
        TypeError: if div is not of int/float type
        ZeroDivisionError: if denominator (div == 0)

    Return:
        New Matrix with results of division
    """
    if (not isinstance(matrix, list) or matrix == [] or matrix is None
            or not all(isinstance(row, list) for row in matrix) 
                or not all(isinstance(items,(int, float))for
                    row in matrix for items in row)):
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    """
    check if items match
    """
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    """check if elements is num type
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    """raise error if denom is 0
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for items in row:
            result = round(items / div, 2)
            new_row. append(result)
        new_matrix.append(new_row)

    return new_matrix
