#!/usr/bin/python3
#  a function that divides 2 integers and prints the result.


def safe_print_division(a, b):
    results = 0
    try:
        results = a / b
    except ZeroDivisionError:
        results = None
    finally:
        print("Inside result: {:d}".format(results))
        return results
