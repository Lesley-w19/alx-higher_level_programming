#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if occur == search else occur for occur in my_list]
