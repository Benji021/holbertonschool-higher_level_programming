#!/usr/bin/python3
def text_indentation(text):
     """
    Prints the input text with 2 new lines after each of the characters: '.', '?', and ':'.

    Args:
    text (str): The text to process and print.

    Raises:
    TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""

    i = 0
    while i < len(text):
        result += text[i]

        if text[i] in '.?':
            result += '\n\n'
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
                result += '\n'
        elif text[i] == ':':
            result += '\n\n'
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
                result += '\n'

        i += 1

    print(result.strip())

text_indentation("Hello world. This is an example text: it should work fine. Have a good day?")
