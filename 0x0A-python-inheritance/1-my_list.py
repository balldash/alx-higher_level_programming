#!/usr/bin/python3

"""
Contains definition for the class MyList that inherits from List.
"""


class MyList(list):
    """
    definition for the class MyList that inherits from List.
    """
    def print_sorted(self):
        """Prints list elements(int) in ascending order"""

        sortedList = sorted(self)
        print(sortedList)
