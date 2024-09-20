#!/usr/bin/python3
"""Define a square"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square with an optimal size

        Args:
            size (int): size of the square
            position (int): position of the square (x, y)

        Raises:
            TypeError: If size is not an interger;
            ValueError: If size is less than 0;
            TypeError: If position is not a tuple of 2 integers;
            ValueError: If position values are less than 0;
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 integers")
        if not all(isinstance(pos, int) for pos in position
            or any(pos < 0 for pos in position):
            raise ValueError
            ("position must be a tuple of 2 no-negative integers")
        self.__position = position

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

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation

        Args:
            value (tuple): the position of the square
  
        Raises:
            TypeError: If value is not a tuple of 2 integers;
            ValueError: If position values are less than 0;
            """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 integers")
        if not all(isinstance(pos, int) for pos in value)
            or any(pos < 0 for pos in value)
        raise ValueError
        ("position must be a tuple of 2 no-negative integers")
        self.__position = value

    def area(self):
        """return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the character #"""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
