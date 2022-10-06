#!/usr/bin/python3
# he Python function def magic_calculation(a, b): bytecode imitate


def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += a ** b / i
        except r as result:
            r = a + b
    return result
