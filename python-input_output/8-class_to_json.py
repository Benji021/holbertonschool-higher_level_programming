#!/usr/bin/python3
"""Module that provides a function to serialize a class instance into JSON-compatible format"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.
    The function assumes all attributes are serializable (list, dict, str, int, bool).
    """
    return {key.lstrip(f"_{obj.__class__.__name__}"): value for key, value in obj.__dict__.items()}
