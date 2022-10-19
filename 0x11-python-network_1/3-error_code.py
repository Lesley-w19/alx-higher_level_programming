#!/usr/bin/python3
"""
3-error_code
"""


from sys import argv
from urllib.error import HTTPError
from urllib.request import urlopen


if __name__ == '__main__':
    base_url = argv[1]
    try:
        with urlopen(base_url) as response:
            content = response.read().decode('UTF-8')
            print(content)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
