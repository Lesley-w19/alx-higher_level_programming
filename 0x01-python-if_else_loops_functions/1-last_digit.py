#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lst = number[-1]
if (lst > 5):
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, lst))
elif (lst < 6 && lst != 0):
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, lst))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, lst))
