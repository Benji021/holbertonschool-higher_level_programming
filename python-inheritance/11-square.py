#!/usr/bin/python3
"""Docstring Rectangle"""


class BaseGeometry:
    """Empty class that defines BaseGeometry"""

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class that defines a rectangle"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Class that defines a square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns the string representation of the square"""
        return f"[Square] {self.__size}/{self.__size}"


if __name__ == "__main__":
    s = Square(5)
    print(s)
    print(s.area())
    print(issubclass(Square, Rectangle))