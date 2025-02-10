#!/usr/bin/python3
"""Docstring Save object to a file"""


import json

def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
