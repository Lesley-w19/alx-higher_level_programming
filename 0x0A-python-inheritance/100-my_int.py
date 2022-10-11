#!/usr/bin/python3
"""
a class MyInt that inherits from int:
"""


class MyInt(int):
    """ a class MyInt that is a rebel"""

    def __eq__(self, obj):
        """ returns is equal to"""
        return super() == obj

    def __ne__(self, obj):
        """ returns not equal to """
        return super() != obj
