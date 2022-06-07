#!/usr/bin/python3
def max_integer(my_list=[]):
    max_number = my_list[0]

    for num in my_list:
        if (num > max_number):
            max_number = num
    print(max_number)
