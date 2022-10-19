#!/usr/bin/python3
"""
7-hbnt-error-code - requests package
"""


from sys import argv
import requests


if __name__ == '__main__':
    base_url = argv[1]
    
    
    try:
        with requests.get(base_url) as response:
            content = response.content.decode("UTF-8")
            print(content)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
