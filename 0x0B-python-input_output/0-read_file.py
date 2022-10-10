#!/usr/bin/python3


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="UTF8") as file:
        readData = file.read()
        print(readData, end="")
    file.close()