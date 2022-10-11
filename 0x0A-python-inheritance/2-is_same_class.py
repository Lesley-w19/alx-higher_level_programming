#!/usr/bin/python3
"""
a function that returns True if the object is exactly
an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """_summary_
    function: object is exactly same as a_class
    Args:
        obj (_type_): object to check
        a_class (_type_): class instance to check
    """
    return type(obj) is a_class
