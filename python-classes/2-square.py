#!/usr/bin/python3
"""Define a square"""


class Square:
    """Empty class that define a square"""

    def __init__(self, size=0):
        """Initialize a new square with an optional size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
