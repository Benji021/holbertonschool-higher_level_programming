#!/usr/bin/python3
"""Docstring class to JSON"""


def class_to_json(obj):
     """
    Function that returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.
    
    Args:
        obj: An instance of a class.
    
    Returns:
        A dictionary representation of the object.
    """

    if not hasattr(obj, "__dict__"):
        return {}

    serialized_dict = {}

    for key, value in obj.__dict__.items():

        if isinstance(value, (list, dict, str, int, bool)):
            serialized_dict[key] = value

    return serialized_dict
