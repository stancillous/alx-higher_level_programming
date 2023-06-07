#!/usr/bin/python3
"""function that prints a square"""


def print_square(size):
    """prints a square

    Args:
        size: square size
    """
    if type(size) != int or (type(size) != int and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        j = 0
        for j in range(0, size):
            print("#", end="")
        print()

