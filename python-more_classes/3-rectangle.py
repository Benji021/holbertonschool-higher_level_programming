#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle

        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle

        Args:
        value (int): the width of the rectangle

        Raises:
        TypeError: If width is not integer;
        ValueError: If width is less than 0;
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Get the height of a rectangle"""
        self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle

        Args:
        value (int): the height of the rectangle

        Raises:
        TypeError: If height is not integer;
        ValueError: If height is less than 0;
        """
        if not isinstance(value, int):
            TypeError("height must be an integer")
        if value < 0:
            ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Checks if width and height are null"""
        if self.__width == 0 or self.__height == 0:
            return ""

        line = "#" * self.__width

        rectangle = [line]
        for _ in range(self.__height):
            rectangle.append(line)
            return '\n'.join(rectangle)
