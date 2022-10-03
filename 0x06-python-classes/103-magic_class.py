#!/usr/bin/python3
""" Write the Python class MagicClass """


import math


class MagicClass:
    """ the Python class MagicClass"""

    __radius = None

    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ returns the area of a circle """
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """ returns the circumference of a circle """
        return math.pi * (self.__radius * 2)
