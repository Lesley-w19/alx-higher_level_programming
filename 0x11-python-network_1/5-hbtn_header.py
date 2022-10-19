#!/usr/bin/python3
"""
5-hbtn-header - package requests
"""


from sys import argv
import requests


if __name__ == '__main__':
    base_url = argv[1]

    with requests.get(base_url) as response:
        content = response.headers['X-Request-Id']
        print(content)
