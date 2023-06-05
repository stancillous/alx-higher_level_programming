#!/usr/bin/python3

"""
Real Definition of a rectangle
"""


class Rectangle:
	"""Class rectangle"""
    
	def __init__(self, width = 0, height = 0):

		""" Method that initializes the instance

        Args:
            width: width of the rectangle
            height: height of the rectangle


        """

		self._width = width
		self._height = height

	@property
	def width(self):
		""" method that returns width value

        Returns:
            width of the rectangle


        """
		return self._width
	
	@width.setter
	def width(self, value):
		""" method that defines the width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero


        """


		if isinstance(value, int) == False:
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		else:
			self._width = value

	@property
	def height(self):
		""" method that returns height value

        Returns:
            height of the rectangle


        """

		return self._height
	
	@height.setter
	def height(self, value):
		""" method that defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero


        """

		if isinstance(value, int) == False:
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		
		self._height = value

