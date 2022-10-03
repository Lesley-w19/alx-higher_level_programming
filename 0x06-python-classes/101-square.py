#!/usr/bin/python3
""" a  class Square that defines a square by: """


class Square:
    """  class Square that defines a square by: """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """ to allow access and to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """ to set the size of the square
        args: value is an integer and must be >= 0

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is not >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ to allow access and to retrieve it """
        return self.__position

    @position.setter
    def position(self, value):
        """ to set the position
        args: value is a tuple of 2 positive integers

        Raises:
        TypeError: position must be a tuple of 2 positive integers
        """
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) and not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0) and (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ that returns the current square area """
        return self.__size ** 2

    def my_print(self):
        """  that prints in stdout the square with the character # """
        if self.__size == 0:
            print()
            return
        for row in range(self.__position[1]):
            print()
        for column in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        result = ""
        if self.size == 0:
            result += ""
        else:
            for row in range(self.position[1]):
                result += "\n"
            for column in range(self.size):
                result += " " * self.position[0]
                result += "#" * self.size
                if (column < self.size - 1):
                    result += "\n"
        return result
