#!/usr/bin/python3
# 7-add_item.py
# Prudence Wambui
"""
script that adds all arguments to a python list
saves them to a file
you need to import:
    sys
    save_to_json_file
    load_from_json_file
"""


import sys
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    """
    load existing items from the file, if it exists
    if file doesnt exist, create an empty one
    add new items from the commandline arguments
    save the updated list to the file
    """
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []
    existing_list.extend(sys.argv[1:])
    save_to_json_file(existing_list, "add_item.json")
