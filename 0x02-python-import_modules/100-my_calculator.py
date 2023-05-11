#!/usr/bin/python3
# authored by  lorna
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    operators = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
    }
    if argv[2] in ops:
        number1 = int(argv[1])
        number2 = int(argv[3])
        ops = operators[argv[2]]
        result = ops(number1, number2)
        print("{:d} {:s} {:d} = {:d}".format(number1, argv[2], number2, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
