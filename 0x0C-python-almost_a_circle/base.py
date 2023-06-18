#!/usr/bin/python3
"""class Base. will be base for all shapes"""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor method for our class"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
