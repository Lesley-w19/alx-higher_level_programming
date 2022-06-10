#!/usr/bin/python3
for alp in reversed(range(97, 123)):
    if alp % 2 == 0:
        print("{:c}".format(alp), end='')
    else:
        print("{:c}".format(alp - 32), end='')
