#!/usr/bin/python3
"""Rectangle"""

class Rectangle:
    """ class Rectangle """
    _Rectangle__width = None
    _Rectangle__height = None

    def __init__(self, widthValue=0, heightValue=0):
        self.width = widthValue
        self.height = heightValue

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

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        result = ""
        if (self.width == 0 or self.height == 0):
            result += ''
        else:
            for row in range(self.height):
                result += "#" * (self.width)
                if (row < self.height - 1):
                    result += '\n'
        return result

    def __del__(self):
        print("Bye rectangle...")
