#!/usr/bin/python3
"""func to append text to file"""


def append_write(filename="", text=""):
    """func to append txt to file
    Args:
        filename: name of file
        text: text to be appended
    Returns:
        number of chars written
    """
    with open(filename, "a", encoding="utf-8") as file:
        chars = file.write(text)
        return chars
