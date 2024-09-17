#!/usr/bin/python3
"""Define a square"""

class Square:
    """Empty class that defines a square"""

    def __int__(self, size=0):
        """Initialize a new square with an optimal size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integers")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        """return the current square area"""
        return self.__size = size ** 2