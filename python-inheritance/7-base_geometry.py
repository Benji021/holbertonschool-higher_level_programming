#!/usr/bin/python3
""" This is the BaseGeometry module """


class BaseGeometry:
    """ Empty class define BaseGeometry """

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
            value(int) : value to be validated
    
        Raises: 
        ValueError : if value is less than or equal to 0
        TypeError : if value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integers")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
