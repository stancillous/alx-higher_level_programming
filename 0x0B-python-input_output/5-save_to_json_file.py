#!/usr/bin/python3
"""importing json module"""
import json

"""func to write json to file"""


def save_to_json_file(my_obj, filename):
    """func to write json to file
    Args:
        my_obj: json obj
        filename: name of file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
