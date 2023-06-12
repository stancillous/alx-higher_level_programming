#!/usr/bin/python3

"""class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """constructor method"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method to return area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """method to return readable str"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
