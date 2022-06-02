#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    rslt = 0
    for n in sys.argv:
        if n != sys.argv[0]:
           rslt += int(n)
    print("{:d}".format(rslt))
