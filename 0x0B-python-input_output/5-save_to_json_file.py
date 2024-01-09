#!/usr/bin/python3
# 5-save_to_json_file.py
# Prudence Wambui
"""
function that writes an object to a text file
using json representation
"""


def save_to_json_file(my_obj, filename):
    """
    import json
    usw w as mode to open file in write only
    write()
    dumps to turn to a json string
    """
    import json

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
