#!/usr/bin/python3
"""func that checks if obj isinstance of class
"""


def is_kind_of_class(obj, a_class):
    
    """ func that checks if obj isinstance of class
    Args:
        obj: object to check
        a_class: class
    Returns: True or False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
