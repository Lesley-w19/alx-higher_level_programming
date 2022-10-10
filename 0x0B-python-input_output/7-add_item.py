#!/usr/bin/python3
"""
Write a script that adds all arguments to a Python list,
and then save them to a file:
"""


import sys


save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file

filename = "add_item.json"

try:
    list_data = load_from_json_file(filename)
except Exception as e:
    list_data = []

for arg in sys.argv[1:]:
    list_data.append(arg)

save_to_json_file(list_data, filename)
