#!/usr/bin/python3
"""Define a class checking function."""

def is_same_class(obj, a_class):
    """Checks if an object is an exact instance of a given class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an exact instance of a_class - True.
        Else - False.
    """
    if type(obj) == a_class:
        return True
    return False
