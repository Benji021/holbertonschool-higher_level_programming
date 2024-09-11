#!/usr/bin/python3
"""
This module contains a function that prints
a square with the character '#'.
"""
def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0 or (isinstance(size, float) and size < 0):
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)