#!/usr/bin/python3

"""
Real definition of a rectangle
"""

class Rectangle:
    """class rectangle"""

    def __init__(self, width = 0, height = 0):
        """init the instance
        Args:
        width: rectangle width
        height: rectangle height

        """

        self._width = width
        self._height = height

        @property
        def width(self):
            """Method to return width value
            Returns:
            width of rectangle
            """

            return self._width

        @width.setter
        def width(self, value):
            """
            defines the width
            Args:
            value: width

            Raise:
            TypeError: width not int
            ValueError: width < 0
            """

            if isinstance(value, int) == False:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self._width = value

            @property
            def height(self):
                """
                method to return height value
                Returns:
                height ofrectangle
                """

                return self._height

            @height.setter
            def height(self, value):
                """
                method to define height
                Args:
                value: height
                Raise:
                TypeError: height not an int
                ValueError: height < 0

                """

                if isinstance(value, int) == False:
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("Height must be >= 0")
                self._height = value
