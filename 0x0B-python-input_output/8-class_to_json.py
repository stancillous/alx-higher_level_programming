#!/usr/bin/python3
"""module to conv class to object"""


def class_to_json(obj):
    """func to convert class obj to json
    Args:
        obj: instance of aclass
    """
    return obj.__dict__
