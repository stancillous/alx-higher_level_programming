#!/usr/bin/python3
"""func to write text to file"""


def write_file(filename="", text=""):
    """
    func to write text to file
    Args:
        filename: name of file
        text: text to be written
    Returns:
        number of chars written
    """
    with open(filename, "w", encoding="utf-8") as file:
        chars = file.write(text)
        return chars
