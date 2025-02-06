#!/usr/bin/python3
""" Module defining the BaseGeometry class """


class BaseGeometry:
    """ Base class for geometric properties. """

    def area(self):
        """
        Raises an Exception with a message indicating that
        the method is not implemented

        Raises:
            Exception: always, as the method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int) -> None:
        """
        Validate that 'value' is a positive integer

        Args:
            name (str) : The name of the variable (always a string)
            value(int) : value to be validated

        Raises:
            TypeError : if value is not an integer
            ValueError : if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
