#!/usr/bin/python3
""" script to add arguments to list and save to a file """


import sys


save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file

filename = "add_item.json"

try:
    list_data = load_from_json_file(filename)
except Exception as e:
    list_data = []

for data in sys.argv[1:]:
    list_data.append(data)
    print(list_data)

save_to_json_file(list_data, filename)
