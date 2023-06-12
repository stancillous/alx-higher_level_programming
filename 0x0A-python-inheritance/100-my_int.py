#!/usr/bin/python3
"""class that inherits from int"""


class MyInt(int):
    """class MyInt"""
    def __eq__(self, other):
        """method to invert =="""
        return not super().__eq__(other)

    def __ne__(self, other):
        """method to invert !="""
        return not super().__ne__(other)
