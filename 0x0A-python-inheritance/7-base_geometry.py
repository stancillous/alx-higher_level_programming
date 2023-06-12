#!/usr/bin/python3
"""class Geometry"""


class BaseGeometry:
    def area(self):
        """func that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ func that validates value
        Args:
        name: string
        value: value to be checked
        Returns: nothing
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than zero".format(name))
