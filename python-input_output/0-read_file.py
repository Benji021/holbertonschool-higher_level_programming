#!/usr/bin/python3
"""Docstring Read file to UTF8"""


def read_file(filename=""):
    """ function opens a file
    Args:
        filename: is the name of the file
    """

    with open(filename, "r", encoding="utf_8") as f:
        content = f.read()
        print(content, end="")
