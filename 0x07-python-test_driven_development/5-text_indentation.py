#!/usr/bin/python3
"""

Module defines a function that indents texts

"""

def text_indentation(text):

    """
    This function prints a text with 2 new lines after each ".", "?", or ":"
   Raises:
        TypeError: If text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    str_output = ''
    delims = ['.', '?', ':']

    for delim in text:
        if delim.isspace() and str_output.endswith('\n'):
            continue
        else:
            str_output += delim
        if delim in delims:
            str_output += '\n\n'
    print(str_output)
