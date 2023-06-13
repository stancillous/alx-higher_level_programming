#!/usr/bin/python3
"""importing json module"""
import json

"""func to load text from json file"""


def load_from_json_file(filename):
    """func to load text from json file
    Args:
        filename: name of file
    """
    with open(filename, encoding="utf-8") as file:
        res = file.read()
        return json.loads(res)
