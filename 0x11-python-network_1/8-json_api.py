#!/usr/bin/python3
"""
8-json-api - packages requests
"""


from sys import argv
import requests


if __name__ == "__main__":
    base_url = 'http://0.0.0.0:5000/search_user'

    if len(argv) >= 2:
        search_letter = argv[1]
    else:
        search_letter = ""

    value = {"q": search_letter}

    with requests.post(base_url, value) as response:
        try:
            content = response.json()

            if len(content) == 0:
                print("No result")
            else:
                print("[{}] {}".format(content['id'], content['name']))
        except ValueError:
            print("Not a valid JSON")
