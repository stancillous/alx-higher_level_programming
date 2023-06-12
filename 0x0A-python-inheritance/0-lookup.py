#!/usr/bin/python3

"""
function that returns the list of available attributes and methods of an object
Args:
    obj: object
Returns: list of atts and methods
"""


def lookup(obj):
    return dir(obj)
