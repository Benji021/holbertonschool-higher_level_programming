#!/usr/bin/python3
"""Docstring Rectangle"""


class BaseGeometry:
    """Empty class that defines BaseGeometry"""
    pass

class Rectangle(BaseGeometry):
    """Define a rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height

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
            name (str): the name of parameter
            value (int): validates value

        Raises:
            TypeError: value is not integer;
            ValueError: value is less or equal to 0;
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    try:
        r = Rectangle(3, 5)
        print(f"Rectangle created: width = {r._width}, height = {r._height}")
        print(issubclass(Rectangle, BaseGeometry))
    except Exception as e:
        print(f"Error: {e}")
