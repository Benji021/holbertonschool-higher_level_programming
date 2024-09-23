#!/usr/bin/python3
"""Defining a class MyList"""


class MyList(list):
    """Class MyList that inherits from list"""

    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
