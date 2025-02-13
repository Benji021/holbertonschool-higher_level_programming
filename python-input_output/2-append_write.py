#!/usr/bin/python3
"Docstring Append to a file to UTF8"


def append_write(filename="", text=""):

    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
