#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num_of_list = 0

    for value in my_list[:x]:
        try:
            print("{:d}".format(value), end='')
            num_of_list += 1
        except ValueError:
            pass
        print()

        return num_of_list
