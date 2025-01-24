#!/usr/bin/python3
"""
This module does X, Y, and Z.
"""


def text_indentation(text):
    """
    Formats the given text by adding two newlines after `.`, `?`, and `:`.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If the input is not a string.

    Returns:
        None: The function prints the formatted text directly.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    skip_space = True

    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
            skip_space = True
        elif char == " " and skip_space:
            continue
        else:
            skip_space = False

        print(result.strip())
