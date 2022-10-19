#!/usr/bin/python3
"""
4-hbnt_status - requests package
"""


import requests


if __name__ == '__main__':
    base_url = 'https://alx-intranet.hbtn.io/status'

    with requests.get(base_url) as response:
        content = response.text
        typeContent = type(content)
        print("Body response:\n\
\t- type: {}\n\t- content: {}".format(typeContent, content))
