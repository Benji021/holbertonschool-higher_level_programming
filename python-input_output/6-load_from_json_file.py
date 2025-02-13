#!/usr/bin/python3
"""Docstring create object from a JSON file"""


import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    
    Args:
        filename (str): The name of the JSON file to read from.
    
    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
