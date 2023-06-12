#!/usr/bin/python3
"""class Square"""

Rectangle = __import__('8-rectangle.py').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """constructor method"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """method to get area of Square"""

        return super().area()
