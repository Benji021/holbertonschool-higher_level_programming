#!/usr/bin/python3
""" This is Docstring Geometry module """


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
    Set a valid value
    
    Args:
        name : my name is John
        value(int) : invaladitated value
    
    Raises: 
    ValueError : if value is less or equal 0
    TypeError : if value is not an integer
    """
    if not isinstance(name, value):
        raise TypeError(f"(name) must be an integers")
    if value <= 0:
        raise ValueError(f"(name) must be greater than 0")
