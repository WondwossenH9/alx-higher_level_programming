#!/usr/bin/python3
"""Define a class Student."""


class Student:
    """Represents the student."""

    def __init__(self, first_name, last_name, age):
        """Initializes the new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets the dictionary representation of the Student.

        If attrs is a list of strings, it represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to be represented.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
