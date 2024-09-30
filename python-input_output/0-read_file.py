#!/usr/bin/python3
"""Docstring Read file to UTF8"""


def read_file(filename=""):

    with open(filename, "r", encoding="utf_8") as f:
        print(f.read())
