#!/usr/bin/python3
"""
6-hbtn-emailpost - requests pckage
"""


from sys import argv
import requests


if __name__ == "__main__":
    base_url = argv[1]
    email = argv[2]
    value = {"email": email}

    with requests.post(base_url, value) as response:
        content = response.content.decode("UTF-8")
        print(content)
