#!/usr/bin/python3
"""
a function that writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """ write a string to a text file """
    nb_characters = 0
    with open(filename, "w", encoding="UTF8") as file:
        nb_characters = file.write(text)
        file.close()
    return nb_characters
