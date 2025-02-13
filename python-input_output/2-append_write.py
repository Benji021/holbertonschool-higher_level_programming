#!/usr/bin/python3
"Docstring Append to a file to UTF8"


def append_write(filename="", text=""):
    """Append a UTF-8 text file and prints its content to stdout"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
