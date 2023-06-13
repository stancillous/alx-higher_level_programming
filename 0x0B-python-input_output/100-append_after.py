#!/usr/bin/python3
"""appends text in a file after each line containing a given string"""


def append_after(filename="", search_string="", new_string=""):
    """appends text in a file after each line containing a given string
    """
    text = ""
    with open(filename) as file1:
        for line in file1:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as fle:
        fle.write(text)
