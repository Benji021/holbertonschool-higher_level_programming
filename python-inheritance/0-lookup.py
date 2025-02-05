#!/usr/bin/python3 
"""This module provides a function to list attributes and methods of an object."""


def lookup(obj):
    """
    Return a liste of available attributes and methods of an object
    
    param obj : the object to inspect
    return : A list of attribute and method names
    """
    return dir(obj)
