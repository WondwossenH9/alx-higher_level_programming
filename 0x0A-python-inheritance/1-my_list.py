#!/usr/bin/python3
"""Define inherited list class MyList."""


class MyList(list):
    """Implement sorted printing for built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
