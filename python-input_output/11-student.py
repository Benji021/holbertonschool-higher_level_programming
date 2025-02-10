#!/usr/bin/python3
"""Docstring Student to disk and reload"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only the attributes included in
        that list will be retrieved. Otherwise, all attributes will
        be retrieved.
        """
        if attrs is None:
            return self.__dict__.copy()

        return {attr: getattr(self, attr) for attr in attrs if attr in self.__dict__}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance from a dictionary.

        Assumes json will always be a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
