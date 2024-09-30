#!/usr/bin/python3
"""Docstring Load, add and save to JSON"""


import json

def save_to_json_file(my_obj, filename):
    """Saves an object to a text file using JSON representation"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

import json

def load_from_json_file(filename):
    """Loads an object from a text file containing JSON representation"""
    with open(filename, 'r') as f:
        return json.load(f)
