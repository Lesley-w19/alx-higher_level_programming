#!/usr/bin/python3
def uniq_add(my_list=[]):
    n_list = set(my_list)
    sum = 0
    for num in n_list:
        sum += num
    return sum
