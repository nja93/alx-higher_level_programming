#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    results = None
    try:
        results = fct(*args)
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
    return results
