#!/usr/bin/python3
""" Function to check if an object is an instance of 
a class that inherited from a specified class """


def inherits_from(obj, a_class):
    """ Check if obj is an instance of a_class that inherited
    directly or indirectly from the specified class 
    """
    return isinstance(obj, a_class) and type(obj) != a_class
