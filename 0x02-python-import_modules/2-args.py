#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv)
    n = len(sys.argv) - 1

    if (n == 0):
        print("{:d} arguments.".format(n))
    elif (n == 1):
        print("{:d} argument:".format(n))
    else:
        print("{:d} arguments:".format(n))
    
    for n in range(1, size):
        print("{:d}: {}".format(n, sys.argv[n]))
