#!/usr/bin/python3

"""
a class Square that defines a square by: (based on 0-square.py)
Private instance attribute: size
Instantiation with size (no type/value verification)
"""


class Square:
    """
    size as a private attribute and instantiation
    """
    def __init__(self, size):
        """_summary_

        Args:
            size (_type_): _size of the square_
        """
        
        self.__size = size
        
    