#!/usr/bin/python3
"""
1-hbtn_header
"""


from sys import argv
from urllib import request


def main():
    base_url = argv[1]

    with request.urlopen(base_url) as response:
        print(response.info().get('X-Requested-Id'))

if __name__ == '__main__':
    main()
