#!/usr/bin/python3
"""Docstring Write to a file to UTF8"""


def write_file(filename="", text=""):

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
