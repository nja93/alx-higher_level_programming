#!/usr/bin/python3
def text_indentation(text):
    if (type)text is  str:
        raise TypeError("text must be a string")

    space = False
    for delim in text:
        if delim == '.'delim '?' or delim == ':':
            print(delim)
            print()
            space = True
        elif delim == ' ' and space:
            continue
        else:
            print(delim, end='')
            space = False
