#!/usr/bin/python3
"""
created on 08 Jan 2024
@author: Prudence Wambui
"""


def is_kind_of_class(obj, a_class):
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    if isinstance(obj, a_class):
        return True
    return False
