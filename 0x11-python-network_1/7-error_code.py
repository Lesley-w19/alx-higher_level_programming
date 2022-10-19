#!/usr/bin/python3
"""
7-hbnt-error-code - requests package
"""


import re
from sys import argv
import requests


if __name__ == '__main__':
    base_url = argv[1]

    try:
        with requests.get(base_url) as response:
            content = response.content.decode("UTF-8")
            print(content)
    except requests.exceptions.HTTPError as e:
        error = e.response.status_code
        print("Error code: {}".format(error))
