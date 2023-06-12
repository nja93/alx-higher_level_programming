#!/usr/bin/python3
"""
Creates a subclass MyList inheriting frm list class
"""


class MyList(list):
    """Child Class MyList inherits frm list"""

    def print_sorted(self):
        """Prints the list, in ascending order"""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
