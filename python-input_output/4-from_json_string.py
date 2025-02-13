#!/usr/bin/python3
"""Docstring from JSON string to object"""


import json

def from_json_string(my_str):
    """Convertit une chaîne JSON en objet Python"""
    return json.loads(my_str)
