#!/usr/bin/python3
"""Define the square"""

class Square:
    def __init__(self, size=0):
        self.__size = size

    def size(self):
        return self.__size
        
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of the square"""
        return self.__size ** 2