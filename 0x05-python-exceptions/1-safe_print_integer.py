#!/usr/bin/python3

def safe_print_integer(value):
    """
    Print an integer with "{:d}".format()

    Args:
        value (int): int to print

    Return:
        False, if TypeError or ValueError occur
        Else - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
