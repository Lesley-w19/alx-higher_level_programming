#!/usr/bin/python3
"""
2-post_email
"""


from urllib import parse, request
from sys import argv


if __name__ == '__main__':

    base_url = argv[1]
    email = argv[2]
    value = {'email': email}

    data = parse.urlencode(value).encode("ascii")

    with request.urlopen(base_url, data) as response:
        content = response.read().decode('UTF-8')

        print(content)
