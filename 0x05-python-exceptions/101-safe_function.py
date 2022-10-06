#!/usr/bin/python3
# a function that executes a function safely.


import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        sys.stderr.write("Exception: ")
        sys.stderr.write(e.args[0])
        sys.stderr.write("\n")
        return None
