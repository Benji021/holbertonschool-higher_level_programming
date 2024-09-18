#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle

        Args:
        width (int): width of rectangle
        height (int): height of rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Get the width of a rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """
            Args:
            value (int): the size of the rectangle

            Raises:
            TypeError : If width is not integer;
            ValueError: If width is less than 0;
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("widht must be >= 0")
            self.__width = value


        @property
        def height(self):
            """Get the height of a rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """
            Args:
            value (int): the size of the rectangle

            Raises:
            TypeError: If height is not integer.
            ValueError: If height is less than 0.
            """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
