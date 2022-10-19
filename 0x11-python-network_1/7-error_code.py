#!/usr/bin/python3
"""
7-hbnt-error-code - requests package
"""


import re
from sys import argv
import requests


if __name__ == '__main__':
    base_url = argv[1]

    with requests.get(base_url) as response:
        error_code = response.status_code
        
        if error_code >= 400:
            print("Error code: {}".format(error_code))
        else:
            content = response.text
            print(content)
