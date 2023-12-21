#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Print an int with "{:d}".format()

    If a ValueError message happens, message print to standard error

    Args:
        value (int): int to print

    Returns:
        If a TypeError or ValueError happens - False
        Else - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
