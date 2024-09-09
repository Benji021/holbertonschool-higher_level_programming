#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return []

    squared_matrix = [[elem ** 2 for elem in row] for row in matrix]

    return squared_matrix
