#!/usr/bin/python3
"""Define a Python class-to-JSON function."""


def class_to_json(obj):
    """Returns a dictionary represntation of a simple data structure."""
    return obj.__dict__
