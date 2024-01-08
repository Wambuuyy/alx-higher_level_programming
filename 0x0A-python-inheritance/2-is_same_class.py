#!/usr/bin/python3
"""
created on 08 Jan 2024
@author: Prudence Wambui
"""


def is_same_class(obj, a_class):
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return type(obj) is a_class
