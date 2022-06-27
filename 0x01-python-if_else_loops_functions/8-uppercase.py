#!/usr/bin/python3
def uppercase(str):
    for alp in str:
        char = ord(alp)
        if (char in range(ord('a'), ord('z') + 1)):
            char -= 32
        print("{:c}".format(char), end='')

    print()
