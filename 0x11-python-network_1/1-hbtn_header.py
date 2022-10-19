#!/usr/bin/python3
"""
1-hbtn_header ---- package urllib
"""


from sys import argv
from urllib import request


if __name__ == '__main__':
    base_url = argv[1]

    with request.urlopen(argv[1]) as response:
        print(response.headers['X-Request-Id'])
