#!/usr/bin/python3
"""
a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file """
    nb_characters = 0
    with open(filename, "a", encoding="UTF8") as file:
        nb_characters = file.write(text)
        file.close()
    return nb_characters
