#!/usr/bin/python3
"""
Write a function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object:
"""


def class_to_json(obj):
    """_summary_
    returns the dictionary description
    with simple data structure
    Args:
        obj (_type_): _JSON serialization of an object in python3
    """
    return obj.__dict__