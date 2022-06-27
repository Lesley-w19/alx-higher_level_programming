#!/usr/bin/python3
for a_lower in range(97, 123):
    if (a_lower != 101 and a_lower != 113):
        print("{:c}".format(a_lower), end='')
