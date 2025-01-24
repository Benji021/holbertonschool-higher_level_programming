#!/usr/bin/python3
"""
This module formats text by adding two newlines after `.`, `?`, and `:`
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
    skip_space = False

    for char in text:
        if skip_space and char == " ":
            continue
        result += char
        skip_space = False
        if char in ".?:":
            result += "\n\n"
            skip_space = True

    result = result.strip()

    for line in result.split("n"):
        print(line.strip())
