#!/usr/bin/python3
"""Define the square"""


class Square:
    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
         """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(Value, int):
            raise TypeError("size must be an integer")
        if Value < 0:
            raise ValueError("size must be >= 0")
        self.__size = Value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
