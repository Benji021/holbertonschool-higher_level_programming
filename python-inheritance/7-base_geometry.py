#!/usr/bin/python3
""" Module defining the BaseGeometry class """


class BaseGeometry:
    """ Base class for geometric properties. """

    def area(self):
        """
        Return current the area that raise an exeption
        with message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that 'value' is a positive integer

        Args:
            name (str) : The name of the variable (always a string)
            value (int) : value to be validated

        Raises:
            TypeError : if value is not an integer
            ValueError : if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
