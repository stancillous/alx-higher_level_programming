#!/usr/bin/python3
"""
function that finds the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in integers list
        If the list is empty, return None
    """
    if len(list) == 0:
        return None
    largest = list[0]
    i = 1
    while i < len(list):
        if list[i] > largest:
            largest = list[i]
        i += 1
    return largest

