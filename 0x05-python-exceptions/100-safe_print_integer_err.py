#!/usr/bin/python3
# a function that prints an integer.


import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Exception: ")
        sys.stderr.write(e.args[0])
        sys.stderr.write("\n")
        return False
