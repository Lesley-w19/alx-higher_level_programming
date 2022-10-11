#!/usr/bin/python3
"""
a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """ class BaseGeometry """
    def area(self):
        """
        public instance method that raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """_summary_
        public method that validate the value
        Args:
            name (_type_): string
            value (_type_): int
        Raises:
        ValueError: if value is not integr
        TypeError: if value is less/equalthan 0
        if not isinstance(value,int):
        """
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
