#!/usr/bin/python3
"""
created on 08 Jan 2024
@author: Prudence Wambui
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    if type(obj) == a_class:
        return True
    return False
