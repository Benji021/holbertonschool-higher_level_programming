#!/usr/bin/python3
"""Docstring Rectangle"""


class BaseGeometry:
    """Empty class that defines BaseGeometry"""

class Rectangle(BaseGeometry):
    """Define a rectangle"""
    def __init__(self, width, height):
        self.__integer_validator("width", width)
        self.__integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return the current area that raises an exeption
        with message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Set that validates value

        Args: 
            name: name is John
            value (int): validates value

        Raises:
        TypeError: value is not integer;
        ValueError: value is less or equal to 0;
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
