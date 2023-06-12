#!/usr/bin/python3
"""func that checks if obj isinstance of class
Args:
    obj: object to check
    a_class: class
Returns: True or False
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
