#!/usr/bin/python3
"""Docstring Rectangle"""


class BaseGeometry:
    """Class that defines BaseGeometry"""

    def integer_validator(self, name, value):
        """
        Validate value

        Args: 
            name (str): the name of the parameter
            value (int): the value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Define a rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a formatted string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"


if __name__ == "__main__":
    try:
        r = Rectangle(3, 5)
        print(f"Rectangle created: width = {r.__width}, height = {r.__height}")
        print(issubclass(Rectangle, BaseGeometry))

        print(f"Area: {r.area()}")

        print(r)

    except Exception as e:
        print(f"Error: {e}")
