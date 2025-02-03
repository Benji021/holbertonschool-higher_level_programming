#!/usr/bin/python3 
"""This is docstring Lookup"""


def lookup(obj):
    """
    Return a liste of available attributes and methods of an object
    
    param obj : the object to inspect
    return : List of attributes and methods an object
    """
    return dir(obj)
