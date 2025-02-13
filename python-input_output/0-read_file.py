#!/usr/bin/python3
"""Docstring Read file to UTF8"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout"""
    try:
        with open(filename, "r", encoding="utf_8") as f:
            print(f.read(), end="")
    except FileNotFoundError:
        print(f"error: file '{filename}' doesn't exist")
    except UnicodeDecodeError:
        print(f"error: do not read '{filename}', encoding problem")
