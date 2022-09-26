#!/usr/bin/python3
""" a class Square that defines a square by:
Private instance attribute
Instantiation with optional
Public instance method
"""


class Square:
    """ a class that defines a square """
    def __init__(self, size=0):
        """ _summary_
        Args:
            size( int, optional). _the size of the square_.Default to 0.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ calculates and Returns the area of the square """
        return self.__size ** 2
