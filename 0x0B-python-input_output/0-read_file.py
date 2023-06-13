#!/usr/bin/python3
"""function to read a text file"""


def read_file(filename=""):
    """function to read a text file
    Args:
        filename: name of file to be read

    """
    with open(filename, encoding="utf-8") as fle:
        print(fle.read(), end='')
