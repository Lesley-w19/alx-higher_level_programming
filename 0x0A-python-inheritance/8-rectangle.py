#!/usr/bin/python3
"""
a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py).
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle """

    def __init__(self, width, height):
        """_summary_
        instantiation method with width and height
        Args:
            width (_type_): positive integer
            height (_type_): positive integer
        width and height must be private. No getter or setter
        width and height must be positive integers, validated
        by integer_validator
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
