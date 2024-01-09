#!/usr/bin/python3
# 6-load_from_json_file.py
# Prudence Wambui
"""
creates an object from json file
"""


def load_from_json_file(filename):
    """
    import json
    open file in read mode
    use load to decode
    """
    import json

    with open(filename) as file:
        return json.load(file)
