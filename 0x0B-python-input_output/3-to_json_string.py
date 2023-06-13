#!/usr/bin/python3
"""importing json module that has the relevant methods"""
import json
"""func to return json string of obj"""


def to_json_string(my_obj):
    """func to convert obj to json string
    Args:
        my_obj: obj to be converted
    """
    res = json.dumps(my_obj)
    return res
