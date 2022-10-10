#!/usr/bin/python3
"""
Write a function that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """_summary_
    funtion creates object from a JSON file
    Args:
        filename (_type_): JSON filename
    """

    with open(filename, 'r') as file:
        data_object = json.loads(file.read())
        file.close()
    return data_object
