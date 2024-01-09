#!/usr/bin/python3
# 4-from_json_string.py
# Prudence Wambui
"""
a function that returns an object
represented by json string
"""


def from_json_string(my_str):
    """
    import json first
    to decode use load()
    """
    import json

    return json.loads(my_str)
