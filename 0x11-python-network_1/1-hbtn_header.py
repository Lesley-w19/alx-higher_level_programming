#!/usr/bin/python3
"""
1-hbtn_header
"""


from sys import argv
from urllib import request


if __name__ == '__main__':
    with request.urlopen(argv[1]) as response:
        print(response.info().get('X-Request-Id'))
