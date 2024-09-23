#!/usr/bin/python3
"""Docstring integer validator"""


class BaseGeometry:
    """Empty class that defines BaseGeometry"""

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
            raise TypeError(f"Expected <name> must be an integer")
        if value < 0:
            raise ValueError(f"Expected <name> must be greater than 0")
