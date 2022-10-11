#!/usr/bin/python3
"""
a function that returns True if the object is an instance of
a class that inherited (directly or indirectly) from the
specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """_summary_
    issubclass -returns whetther its derived form same or other class
    Args:
        obj (_type_): object to be inherited
        a_class (_type_): class to be checked
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
