#!/usr/bin/python3
"""
created on 08 Jan 2024
authoor: Prudence Wambui
"""


class MyList(list):
    """
    inherits from class list
    """

    def print_sorted(self):
        """
        prints the list
        but in asceding sort
        """
        print(sorted(self))
