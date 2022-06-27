#!/usr/bin/python3
"""Rectangle class"""

class Rectangle:
    """class Rectangle defines a rectangle with bases"""
    widthVal = None
    heightVal = None

    def __init__(self, width=0, height=0):
        self.widthVal = width
        self.heightVal = height

    @property
    def width(self):
        return self.widthVal

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.widthVal = value

    @property
    def height(self):
        return self.heightVal

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.heightVal = value
