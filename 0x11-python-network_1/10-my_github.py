#!/usr/bin/python3
"""
10-my-github - packages requests
"""


from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if '__name__' == '__main__':
    base_url = 'https://api.github.com/user'

    user = argv[1]
    p_wrd = argv[2]

    with requests.get(base_url, auth=HTTPBasicAuth(user, p_wrd)) as response:
        content = response.json()
        print("{}".format(content.get('id')))
