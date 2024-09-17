#!/usr/bin/python3
"""Define the square"""

class Square:
    def __init__(self, size=0):
        self.size = size

    def size(self):
        """Retrieve the size of the square"""
        return self.__size
        
    def size(self, value):
        """Set the size of the square with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2