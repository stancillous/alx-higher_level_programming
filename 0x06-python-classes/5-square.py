#!/usr/bin/python3
"""creating a new class"""


class Square:
    """
    new Square class
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return self.__size * self.__size
    
    @property
    def size(self):
        """function to retrieve value of size"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """function to set value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def my_print(self):
        """function that prints square with # symbols"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
