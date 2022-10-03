#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0

    for value in my_list[:x]:
        try:
            print("{:d}".format(value), end='')
            num += 1
        except (TypeError, ValueError):
            continue
    print()
    return num
