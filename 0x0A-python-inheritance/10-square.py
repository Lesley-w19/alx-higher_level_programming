#!/usr/bin/python3
"""
a class Square that inherits from Rectangle
(9-rectangle.py):
"""
Rectangle = __import__("9-rectangle").Rectangle


class Sqaure(Rectangle):
    """ class square """

    def __init__(self, size):
        """_summary_
        instantiation method with size
        Args:
            size (_type_): positive integer
        size must be private. No getter or setter
        size must be a positive integer, validated
        by integer_validator
        """

        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """ area method must be implemented"""
        result = self.__size ** 2
        return result
