#!/usr/bin/env python3
"""Docstring Pascal's Triangle"""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row.
    
    Args:
        n (int): Number of rows in the triangle.
    
    Returns:
        List[List[int]]: Pascal's triangle as a list of lists.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
