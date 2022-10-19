#!/usr/bin/python3
"""
0-hbtn_status
"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        typeContent = type(content)
        ut8Content = content.decode('UTF-8')

        print("Body response:\n\
\t- type: {}\n\t- content: {}\n\t- utf8 content: {}\
".format(typeContent, content, ut8Content))
