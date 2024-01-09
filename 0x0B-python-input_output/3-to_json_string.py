#!/usr/bin/python3
# 3-to_json_string.py
# Prudence Wambui
"""
function that returns the JSON
representation of an object
"""


def to_json_string(my_obj):
    """
    first import json to be able to use it
    use dumps to encode
    """
    import json

    return json.dumps(my_obj)
