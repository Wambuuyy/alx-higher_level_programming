#!/usr/bin/python3


def uppercase(str):
    for char in str:
        char_code = ord(char)
        if 97 <= char_code <= 122:#check if liwercase
            char_code -= 32#convert upper
            print("{:c}".format(char), end="")
        else:
            print(char, end="")
    print()
