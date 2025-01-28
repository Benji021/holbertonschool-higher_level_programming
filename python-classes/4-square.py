#!/usr/bin/python3
"""Define a square"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """
        Initialize a new square with an optimal size

        Args:
            size (int): size of the square

        Raises:
            TypeError: If size is not an interger;
            ValueError: If size is less than 0;
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation

        Args:
            value (int): the size of the square

        Raises:
            TypeError: If size is not an integer;
            ValueError: If size is less than 0;
        """
        if not isinstance(value, int):
            TypeError("size must be an integer")
        if value < 0:
            ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current square area"""
        return self.__size ** 2
