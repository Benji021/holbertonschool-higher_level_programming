#!/usr/bin/python3
"""Defines a square"""


class Square:
    """defines a square"""

    def __init__(self, size):
        """
        Initializes the square with a private size attribute

        Args:
        size (int): size of the square
        """
        self.__size = size
