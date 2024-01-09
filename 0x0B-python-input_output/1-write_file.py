#!/usr/bin/python3
# 1-write_file.py
# Prudence Wambui
"""
function that writes a string to a text file
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    the mode of the file opening should be w
    it creates a file if it doesnt exist
    overwrites if it already existed
    write() returns number of characters written
    """
    with open(filename, 'w', encoding="UTF-8") as file:
        characters = file.write(text)
        return characters
