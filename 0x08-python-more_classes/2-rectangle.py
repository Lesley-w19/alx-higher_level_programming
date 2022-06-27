#!/usr/bin/python3
"""Rectangle"""

class Rectangle:
    """class Rectange with private and public instances"""
    
    _Rectangle__height = None
    _Rectangle_width = None

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
            raise ValueError("height must be  >= 0")
        self._Rectangle__height = value

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be  >= 0")
        self._Rectangle__width = value

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        if (self.height == 0 or self.width == 0):
            return 0
        else:
            return (self.height + self.width) * 2
