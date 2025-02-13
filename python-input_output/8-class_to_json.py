#!/usr/bin/python3
"""Module that provides a function to serialize a class instance into JSON-compatible format"""


import json
def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.
    The function assumes all attributes are serializable (list, dict, str, int, bool).
    """
    try:
        return json.loads(json.dumps(obj.__dict__))
    except AttributeError:
        raise TypeError(f"Object of type {type(obj).__name__} is not serializable")
