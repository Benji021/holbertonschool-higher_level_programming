#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    
    param obj: the object to inspect.
    return: List of attribute and method names.
    """
    return dir(obj)