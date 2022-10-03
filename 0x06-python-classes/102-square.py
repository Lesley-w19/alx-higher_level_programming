#!/usr/bin/python3
"""  a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """ defines a square by size (int, default to zero).
    use setters
    instantiation of square and area as public instance
    """
    def __init__(self, size=0):
        """ define size"""
        self.size = size

    @property
    def size(self):
        """ returns and Allows access of the private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args: size to int. Default to 0.
        Raises:
        TypeError: if size is not an integer
        ValueError: if size is not >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ calculates the area of the square using the size"""
        return self.__size ** 2

    def __eq__(self, value):
        if not isinstance(value, Square):
            raise TypeError("the value should be a square-type object")
        return self.size == value.size

    def __ne__(self, value):
        if not isinstance(value, Square):
            raise TypeError("the value should be a square-type object")
        return self.size != value.size

    def __gt__(self, value):
        if not isinstance(value, Square):
            raise TypeError("the value should be a square-type object")
        return self.size > value.size

    def __lt__(self, value):
        if not isinstance(value, Square):
            raise TypeError("the value should be a square-type object")
        return self.size < value.size

    def __ge__(self, value):
        if not isinstance(value, Square):
            raise TypeError("the value should be a square-type object")
        return self.size >= value.size

    def __le__(self, value):
        if not isinstance(value, Square):
            raise TypeError("the value should be a square-type object")
        return self.size <= value.size
