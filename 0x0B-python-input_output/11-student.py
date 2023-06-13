#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that returns__dict__"""
        new_dict = {}
        if type(attrs) == list:
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict
        return self.__dict__
    def reload_from_json(self, json):
        """method to replace obj attrs"""
        self.__dict__ = json
