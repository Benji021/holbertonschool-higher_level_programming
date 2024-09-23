#!/usr/bin/python3
"""Docstring for exact same object"""


def is_same_class(obj, a_class):
    """
    Function return True if the object is exactly
    an instance of specified class
    otherwise False
    """
    return type(obj) is a_class
