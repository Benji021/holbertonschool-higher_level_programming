#!/usr/bin/python3
"""Docstring create object from a JSON file"""


def load_from_json_file(filename):
    with open(filename, "r") as file:
        return json.load(file)
