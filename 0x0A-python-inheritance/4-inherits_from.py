#!/usr/bin/python3
"""
created on 08 Jan 2024
@author:Prudence Wambui
"""


def inherits_from(obj, a_class):
    """
    a function that checks if an object is an instance
    of a class that inherited from a specified class
    either directly or indirectly
    returns true or false accordingly
    """
    if issubclass(type(obj), a_class) and type(obj != a_class):
        return True
    return False
