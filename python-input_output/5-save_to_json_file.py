#!/usr/bin/python3
"""Docstring Save object to a file"""


import json

def save_to_json_file(my_obj, filename):
    with open(filename, "w") as file:
        json.dump(my_obj, file)
