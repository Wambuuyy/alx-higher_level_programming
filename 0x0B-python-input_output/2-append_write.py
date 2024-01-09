#!/usr/bin/python3
# 2-append_write.py
# Prudence Wambui
"""
function that appends a string at the end of the text file
returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    to append use the'a' mode while opening the file
    write() returns number of characters written
    """
    with open(filename, 'a', encoding='UTF-8') as file:
        return (file.write(text))
