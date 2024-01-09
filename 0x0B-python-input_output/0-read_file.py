#!/usr/bin/python3
# 0-read_file.py
# Prudence Wambui
"""
a function that reads a textfile and prints it
"""


def read_file(filename=""):
    """
    uses utf-8 encoding
    input required is filename only
    so it defaults the mode to read
    """
    with open(filename, encoding="UTF-8") as file:
        print(file.read(), end='')
