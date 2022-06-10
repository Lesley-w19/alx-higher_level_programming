#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if (number == 0):
    printf("{:d} is zero".format(number))
elif (number < 0):
    printf("{:d} is negative".format(number))
else:
    printf("{:d} is positive".format(number))
