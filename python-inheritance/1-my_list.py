#!/usr/bin/python3
"""Defining a class MyList that inherits from list."""


class MyList(list):
    """ Define MyList that inheritance list """

    def print_sorted(self):
        """ Print the list, but sorted ascensing sort """
    
        if len(self) == 0:
            print([])
        else:
            print(sorted(self))