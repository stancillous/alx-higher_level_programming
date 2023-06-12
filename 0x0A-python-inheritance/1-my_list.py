#!/usr/bin/python3
"""
class  that inherits from list
"""


class MyList(list):
    def print_sorted(self):
        """
        func that returns sorted list
        """
        sorted_list = sorted(self)
        return(sorted_list)
