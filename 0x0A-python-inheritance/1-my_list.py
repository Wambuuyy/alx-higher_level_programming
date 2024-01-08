#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 08 Jan 2024

@author: Prudence Wambui
"""


class MyList(list):
    """
     class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints sorted list
        """
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
