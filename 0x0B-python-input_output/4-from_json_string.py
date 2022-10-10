#!/usr/bin/python3
"""
a function that returns an object (Python data structure)
represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """_summary_
    returns an object (Python data structure)JSON from Python
    Args:
        my_str (_type_): _description_
    """
    return json.loads(my_str)
