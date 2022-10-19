#!/usr/bin/python3
"""
10-my-github - packages requests
"""


from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if '__name__' == '__main__':
    base_url = 'https://api.github.com/user'

    username = argv[1]
    password = argv[2]

    with requests.get(base_url, auth=HTTPBasicAuth(username, password)) as response:
        content = response.json()
        user_id = content.get('id')
        print(user_id)
