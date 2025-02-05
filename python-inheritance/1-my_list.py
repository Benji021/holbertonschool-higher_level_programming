#!/usr/bin/python3
""" This is docstring MyList"""


class MyList(list):
    """ Define MyList that inheritance list """

    def print_sorted(self):
        """ Print the list, but sorted ascensing sort """
        print(sorted(self))

if __name__ == "__main__":
    my_list = MyList([3, 1, 4, 1, 5, 9, 2, 6])
    my_list.print_sorted()  # Affichera la liste triée
