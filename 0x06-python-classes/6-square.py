#!/usr/bin/python3
""" a class Square that defines a square by: (based on 5-square.py) """


class Square:
    """ defines a square with size and position """
    def __init__(self, size=0, position=(0, 0)):
        """
        args: position and size
        """
        self.size = size
        self.postion = position

    @property
    def size(self):
        """ retrieves and allows acces of size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size attribute
        args: value is to be an integer
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
        """ retrieves and allows acces of position attribute """
        return self.__position

    @position.setter
    def postion(self, value):
        """
        args: must be a tuple of 2 positive integers,
        Raises:
        TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if ((value[0] < 0) and (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns the current square area """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for row in range(self.__position[1]):
                print()
            for cl in range(self.__size):
                print("" * self.__position[0] + "#" * self.__size)
