#!/usr/bin/python3
"""
100-my-github - packages requests
"""


from sys import argv
import requests


if __name__ == '__main__':
    repo_name = argv[1]
    repo_owner = argv[2]

    base_url = "https://api.github.com/repos/{}/{}/commits".format(
            repo_name, repo_owner)

    with requests.get(base_url) as response:
        content = response.json()

        if (len(content) == 0):
            print("No result")
        else:
            for infos in content:
                print(
                    "{}: {}".format(infos.get('sha'),
infos.get('commit').get('author').get('name')))
