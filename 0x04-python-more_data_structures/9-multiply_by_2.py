#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied_dict_key = {}
    for key, value in a_dictionary.items():
        multiplied_dict_key[key] = value * 2
           return multiplied_dict_key
