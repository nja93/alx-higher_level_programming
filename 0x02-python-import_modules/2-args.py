#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg = sys.argv
    size = len(arg) - 1

    if size == 0:
        print("{} arguments.".format(size))

    elif size > 1:
        print("{} arguments:".format(size))
        for r in range(1, size + 1):
            print("{}: {}".format(r, arg[r]))

    else:
        print("{} argument:".format(size))
        print("{}: {}".format(size, arg[1]))
