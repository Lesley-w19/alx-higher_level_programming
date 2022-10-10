#!/usr/bin/python3
"""
a function that writes an Object to a text file, using a JSON representation:
"""
from dataclasses import field
import json


def save_to_json_file(my_obj, filename):
    """_summary_
    function that writes an Object to a text file,
    using a JSON representation
    Args:
        my_obj (_type_): object in JSON format
        filename (_type_): new filename to write
    """
    file_data = json.dumps(my_obj)
    with open(filename, 'w') as file:
        file.write(file_data)
        file.close()
