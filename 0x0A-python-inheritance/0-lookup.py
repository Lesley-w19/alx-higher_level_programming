#!/usr/bin/python3
"""
a function that returns the list of available
attributes and methods of an object:
"""


def lookup(obj):
    """_summary_

    Args:
        obj (_type_): the list attribute of the object
    """
    return list(dir(obj))
