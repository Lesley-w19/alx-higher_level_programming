#!/usr/bin/python3
"""Rectangle class"""

class Rectangle:
    """class Rectangle defines a rectangle with bases"""
    _Rectangle__height = None
    _Rectangle__width = None

    def __init__(self, widthVal=0, heightVal=0):
        self.height = heightVal
        self.width = widthVal

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >=0")
        self._Rectangle__height = value

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value
