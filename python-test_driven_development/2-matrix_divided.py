#!/usr/bin/python3
def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(element, (int, float)) for row in matrix for element in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
