#!/usr/bin/python3
"""
a function that returns the JSON representation of an
object (string):
"""
import json


def to_json_string(my_obj):
    """_summary_'
    returns json representation of an object (string):

    Args:
        my_obj (_type_): _description_
    """
    return json.dumps(my_obj)
