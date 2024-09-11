#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    skip_space = True  # Flag to skip spaces at the beginning of a new sentence

    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
            skip_space = True  # We want to skip spaces after these characters
        elif char == " " and skip_space:
            # Skip the space after punctuation
            continue
        else:
            skip_space = False

    # Print the result without leading/trailing spaces on each line
    print(result.strip()