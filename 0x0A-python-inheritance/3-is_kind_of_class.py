#!/usr/bin/python3
"""
is an instance
a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """_summary_
    function: object isinstance as a_class
    Args:
        obj (_type_): the object checked
        a_class (_type_): the class to be compared
    """
    return isinstance(obj, a_class)
