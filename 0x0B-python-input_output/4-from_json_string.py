#!/usr/bin/python3
"""importing module with relevant json methods"""
import json

"""func to converte json string to obj"""


def from_json_string(my_str):
    """func to convert json str to obj
    Args:
        my_str: json str
    """
    return json.loads(my_str)
