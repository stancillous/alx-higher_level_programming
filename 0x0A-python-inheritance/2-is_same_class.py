#!/usr/bin/python3
"""
func to check if obj is exactly of given class
Args:
    obj: object to be checked
    a_class: class
Returns: True or False
"""


def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
