#!/usr/bin/python3
"""class Square"""

Rectangle = __import__('8-rectangle.py').Rectangle


class Square:
    """class Square"""

    def __init__(self, size):
        """constructor method"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """method to get area of Square"""

        return self.__size * self.__size
