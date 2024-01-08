#!/usr/bin/python3
"""
created on 08 Jan 2024
authoor: Prudence Wambui
"""


class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
