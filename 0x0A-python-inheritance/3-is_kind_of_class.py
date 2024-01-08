#!/usr/bin/python3
"""
created on 08 Jan 2024
@author: Prudence Wambui
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    if isinstance(obj, a_class):
        return True
    return False
