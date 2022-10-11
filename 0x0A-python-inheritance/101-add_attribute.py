#!/usr/bin/python3
"""
a function that adds a new attribute to an object if it’s possible:
"""


def add_attribute(obj, name, value):
    """_summary_
    a function that adds a new attribute to an object
    Args:
        obj (_type_): object to add
        name (_type_): string
        value (_type_): integer
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
