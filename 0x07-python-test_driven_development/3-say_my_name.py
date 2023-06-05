#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    function that prints first and last names

    args: first name & last name
    Raise:
    TypeError: When value entered is not if type str

    """ 

    if type(first_name) is not str:
        raise TypeError ("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError ("last_name must be a string")
     
    print("My Name is {} {}".format(first_name, last_name))
