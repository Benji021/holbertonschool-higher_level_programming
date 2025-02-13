#!/usr/bin/python3
"""Docstring Write to a file to UTF8"""


def write_file(filename="", text=""):
    """Write a UTF-8 text file and prints its content to stdout"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
