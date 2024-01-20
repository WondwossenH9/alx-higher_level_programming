#!/usr/bin/python3
# 6-from_json_string.py
"""Define a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Returns the Python object representation of the JSON string."""
    return json.loads(my_str)
