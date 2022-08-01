#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num_of_list = 0

    for value in range(x):
        try:
            print("{}".format(my_list[value]), end='')
        except:
            break
        else: 
            num_of_list += 1

        print()
        return num_of_list
