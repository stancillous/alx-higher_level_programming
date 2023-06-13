#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method that returns __dict__"""
        return self.__dict__
