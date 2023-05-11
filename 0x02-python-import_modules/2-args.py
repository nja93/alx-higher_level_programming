#!/usr/bi/python3

if __name__ == "__main__":
    import sys

    arg = sys.argv
    size = len(arg) - 1

    if size == 0:
    print("{} arguments.".format(size))

    elif size > 1:
        print("{} arguments:".format(size))
        for x in range(1, size + 1):
            print("{}: {}".format(i, arg[i]))

    else:
        print("{} argument:".format(size))
        print("{}: {}".format(size, arg[1]))
