#!/usr/bin/python3
""" This is docstring MyList"""


class MyList(list):
    """ Define MyList that inheritance list """

    def print_sorted(self):
        """ Print the list, but sorted ascensing sort """
        print(sorted(self))
