#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for items in range (0,x)
            print("{:d}".format(my_list[items]), end="")
            count += 1
    except (ValueError, TypeError):
            continue
    print()
    return count
