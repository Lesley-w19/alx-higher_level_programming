#!/usr/bin/python3
"""
0-hbtn_status
"""
from urllib import request


if __name__ == '__main__':
   with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    ut8Content = content.decode('utf-8')

    print("Body response:\
        \n\t- type: {}\
        \n\t- content: {}\
        \n\t- utf8 content: {}\
        ".format(type(content), content, ut8Content)
        )
