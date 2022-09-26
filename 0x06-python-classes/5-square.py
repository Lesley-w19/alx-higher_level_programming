#!/usr/bin/python3
""" a class Square that defines a square by: (based on 4-square.py) """


class Square:
    """ a class Square that defines a square by instance attribute size
uses setters and getters to set and retrieve size int
"""
    def __init__(self, size=0):
        """ define the size attribute"""
        self.size = size

    @property
    def size(self):
        """ retrieves and allows access to the size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args: value: the size attribute.
        Riases:
        TypeError: if value is not an integer
        ValueError: if value is not >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """  that returns the current square area """
        return self.__size ** 2

    def my_print(self):
        """ that prints in stdout the square with the character # """
        for i in range(self.__size):
            print("#" * self.__size)
        if (self.__size == 0):
            print()
