#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    n = len(sys.argv) - 1
    if (n != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator == '+':
        rslt = add(a, b)
    elif operator == '-':
        rslt = sub(a, b)
    elif operator == '/':
        rslt = div(a, b)
    elif operator == '*':
        rslt = mul(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, rslt))
