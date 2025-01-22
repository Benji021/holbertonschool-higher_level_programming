#!/usr/bin/python3
"""
This is a docstring.
"""
def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Parameters:
    a : int or float : First number.
    b : int or float : Second number (default is 98).

    Returns:
    int : Sum of a and b, after converting to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
