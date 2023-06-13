#!/usr/bin/python3
"""importing json module"""
import json

"""func to convert class obj to json"""


def class_to_json(obj):
    """func to convert class obj to json
    Args:
        obj: instance of aclass
    """
    dict = {}
    if hasattr(obj, "__dict__"):
        dict = obj.__dict__.copy()
    return dict_
