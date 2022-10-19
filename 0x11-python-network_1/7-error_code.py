#!/usr/bin/python3
"""
7-hbnt-error-code - requests package
"""


from sys import argv
import requests


if __name__ == '__main__':
    base_url = argv[1]
    with requests.get(base_url) as response:
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)
