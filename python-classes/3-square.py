#!/usr/bin/python3
"""Define a square"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initialize a new square with an optimal size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the current square area"""
        return self.__size ** 2
