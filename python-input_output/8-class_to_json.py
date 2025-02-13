#!/usr/bin/python3
"""Module that provides a function to serialize a class instance into JSON-compatible format"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.
    The function assumes all attributes are serializable (list, dict, str, int, bool).
    """
    return obj.__dict__
