#!/usr/bin/python3
""" This is a Docstring Only sub class of """


def inherits_from(obj, a_class):
    """ Ckeck if obj is an instance of a_class that inherited
    directly or indirectly from the specified class 
    """
    return isinstance(obj, a_class) and type (obj) is not a_class
