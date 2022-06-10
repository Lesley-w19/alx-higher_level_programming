#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
#to get last digit of number; the remainder after dividing by 10
if number < 0:
    lst = number % -10
else:
    lst = number % 10
print("Last digit of {:d} is {:d}".format(number, lst), end = "")
if (lst > 5):
    print("and is greater than 5")
elif (lst == 0):
    print("and is 0")
elif (lst < 6 and lst != 0):
    print("and is less than 6 and not 0")
